import pygame as pg
import sys
import time

def main():
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ!こうかとん")
    screen = pg.display.set_mode((1600,900))    #画面用Surface
    sc_rect = screen.get_rect()                 #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")     #背景画像用Surface
    bg_rect = bg_img.get_rect()                 #背景画像用rect
    #bg_rect.center = (1500,500)
    screen.blit(bg_img,bg_rect)                 #背景画像用Surfaceを画面用Surfaceに貼り付ける

    #練習３
    tori_img = pg.image.load("fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 4.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    

    while True :
        #練習２
        screen.blit(bg_img, bg_rect)
        screen.blit(tori_img, tori_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return

    
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()