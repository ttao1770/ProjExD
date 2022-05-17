import random
import pygame as pg
import sys
import time

key__delta = {  pg.K_UP : [0, -1],
                pg.K_DOWN : [0, +1],
                pg.K_LEFT : [-1, 0],
                pg.K_RIGHT : [+1, 0],}

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ!こうかとん")
    screen = pg.display.set_mode((1600,900))        #画面用Surface
    sc_rect = screen.get_rect()                     #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像用Surface
    bg_rect = bg_img.get_rect()                     #背景画像用rect
    #bg_rect.center = (1500,500)
    screen.blit(bg_img,bg_rect)                     #背景画像用Surfaceを画面用Surfaceに貼り付ける

    #練習３
    tori_img = pg.image.load("fig/6.png")           #こうかとん画像用Surface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()                 #こうかとん画像用rect
    tori_rect.center = 900, 400                     #こうかとん画像用Surfaceを画面用Surfaceに貼り付ける
    screen.blit(tori_img, tori_rect)

    #練習5
    bomb = pg.Surface((20,20))                      #爆弾用Surface
    bomb.set_colorkey((0))
    pg.draw.circle(bomb, (255,0,0), (10,10), 10)    #爆弾用Surfaceに円を描く
    bomb_rect = bomb.get_rect()
    
    bomb_x,bomb_y = random.randint(0,sc_rect.width),random.randint(0,sc_rect.height)
    while 700 <= bomb_y <= 100 and 300 <= bomb_y <= 500 :
        bomb_x,bomb_y = random.randint(0,sc_rect.width),random.randint(0,sc_rect.height)
    bomb_rect.center =  bomb_x,bomb_y
    screen.blit(bomb, bomb_rect)                    #爆弾用Surfaceを画面用Surfaceに貼り付ける

    vx, vy = +1, +1
    while True :
        #練習２
        screen.blit(bg_img, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #練習4
        key_states = pg.key.get_pressed()
        for key, delta in key__delta.items():
            if key_states[key] == True : 
                tori_rect.centerx += delta[0] 
                tori_rect.centery += delta[1] 
                if check_bound(sc_rect, tori_rect) != (1, 1):
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img, tori_rect)

        #練習6
        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb, bomb_rect)
        x,y = check_bound(sc_rect, bomb_rect)
        vx *= x
        vy *= y

        # 練習8
        if tori_rect.colliderect(bomb_rect): return 
        #　こうかとん用のRectが爆弾用のRectと衝突していたらreturn
        
        pg.display.update()
        clock.tick(1000)

def check_bound(sc_r, obj_r):   #画面用Rect, {こうかとん,　爆弾}Rect
    #画面内:+1 / 画面外:-1
    x, y = 1, 1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1
    return x, y

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()