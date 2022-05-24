import pygame as pg
import sys
import random
import math

c = 0
ax = 1/300
ay = 1/300

class Screen:
    def __init__(self, fn, wh, title):
        # fn:背景画像のパス, wh:幅高さのタプル, title:画面のタイトル
        pg.display.set_caption(title)
        self.width, self.height = wh #(1600, 900)
        self.disp = pg.display.set_mode((self.width, self.height)) #Surface
        self.rect = self.disp.get_rect() # Rect
        self.image = pg.image.load(fn) # Surface


class Bird(pg.sprite.Sprite):
    key_delta = {pg.K_UP   : [0, -20],
                pg.K_DOWN : [0, +20],
                pg.K_LEFT : [-20, 0],
                pg.K_RIGHT: [+20, 0],}

    def __init__(self, fn, r, xy):
        super().__init__()
        # fn:画像のパス, r:画像の拡大率, xy:画像の初期座標のタプル
        self.image = pg.image.load(fn) # Surface
        self.image = pg.transform.rotozoom(self.image, 0, r)
        self.rect = self.image.get_rect() # Rect
        self.rect.center = xy

    def update(self,screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1] 
                # 練習7
                if check_bound(screen.rect, self.rect) != (1,1): 
                    self.rect.centerx -= delta[0]
                    self.rect.centery -= delta[1]


class Bomb(pg.sprite.Sprite):
    def __init__(self, col, r, vxy, screen):
        super().__init__()
        # color:爆弾の色, r:爆弾の半径, vxy:爆弾の速度タプル, screen描画用Screenオブジェクト
        self.image = pg.Surface((r*2,r*2)) # 爆弾用のSurface
        self.image.set_colorkey((0,0,0)) # 黒色部分を透過する
        pg.draw.circle(self.image, col, (r,r), r)
        self.rect = self.image.get_rect()                    # 爆弾用Rect
        self.rect.centerx = random.randint(0, 100)
        self.rect.centery = random.randint(0, 100)
        self.vx, self.vy = vxy
    
    def update(self, screen):
        global ax,ay,c
        ax += math.sin(c)/1000
        ay += math.cos(c)/1000
        self.rect.move_ip(self.vx, self.vy)
        x, y = check_bound(screen.rect, self.rect)
        self.vx += abs(ax) * x
        self.vx += abs(ay) * y
        self.vx *= x # 横方向に画面外なら，横方向速度の符号反転
        self.vy *= y # 縦方向に画面外なら，縦方向速度の符号反転


def start():
    clock = pg.time.Clock()

    screen = Screen("fig/x.PNG", (1600,900), "start")
    screen.disp.blit(screen.image, (0,0))
    while True :
        screen.disp.blit(screen.image, screen.rect)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        pg.display.update()  # 画面の更新
        clock.tick(1000)



def main():
    global ax,ay,c
    clock = pg.time.Clock()
    
    # 練習1
    screen = Screen("fig/pg_bg.jpg", (1600,900), "逃げろ！こうかとん")
    screen.disp.blit(screen.image, (0,0))

    # 練習3
    bird = Bird("fig/3.png", 2, (900, 400))
    screen.disp.blit(bird.image, bird.rect)
    # こうかとん画像用のSurfaceを画面用Surfaceに貼り付ける
    birds = pg.sprite.Group()
    #for _ in range(19):
    birds.add(Bird("fig/3.png", 2, (int(random.randint(1,200))/100*700+200, int(random.randint(1,200))/100*300+200)))

    # 練習5
    bomb = Bomb((255,0,0), 10, (+2, +2), screen)
    screen.disp.blit(bomb.image, bomb.rect)
    # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
    bombs = pg.sprite.Group()
    for i in range(10):
        bombs.add( Bomb((255,0,0), 10, (math.sin(90*i)+4, math.cos(90*i)+4), screen))


    while True:
        c += 1
        # 練習2
        screen.disp.blit(screen.image, screen.rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return       # ✕ボタンでmain関数から戻る

        # 練習4
        birds.update(screen)
        #screen.disp.blit(bird.image, bird.rect)
        birds.draw(screen.disp)

        # 練習6
        bombs.update(screen)
        #screen.disp.blit(bomb.image, bomb.rect)
        bombs.draw(screen.disp)

        # 練習8
        if len(pg.sprite.groupcollide(birds, bombs, False, False)) != 0: return
        #if pg.sprite.collide_rect(bird, bomb) : return
        # こうかとん用のRectが爆弾用のRectと衝突していたらreturn

        pg.display.update()  # 画面の更新
        clock.tick(1000)
 
    
# 練習7
def check_bound(sc_r, obj_r):   #画面用Rect, {こうかとん,　爆弾}Rect
    #画面内:+1 / 画面外:-1
    x, y = 1, 1
    #爆弾の弾道を変則にした
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x= -1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y= -1
    return x, y


if __name__ == "__main__":
    pg.init() 
    start()
    main()
    pg.quit()
    sys.exit()