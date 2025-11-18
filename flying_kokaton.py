import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))        
    
    
    #pg.display.update()
    #enn=pg.Surface((20,20))
    #pg.draw.circle(enn,(255,0,0),(10,10),10)
    #txt = fonto.render("hello",True,(255,255,255))

    
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    #こうかとん
    img = pg.image.load("fig/3.png")
    img = pg.transform.flip(img,True,False)
    img_rct = img.get_rect()
    img_rct.center=300,200
        
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        #背景

        x=tmr%3200
        kk_img = pg.image.load("fig/pg_bg.jpg")
        #kk_img = pg.transform.scale(kk_img,(800,900))
        screen.blit(kk_img,[-x,0])

        kk_img2=pg.image.load("fig/pg_bg.jpg")
        kk_img2=pg.transform.flip(kk_img2,True,False)
        screen.blit(kk_img2,[-x+1600,0])

        kk_img3 = pg.image.load("fig/pg_bg.jpg")
        screen.blit(kk_img3,[3200-x,0])

        #txt = font.render(str(tmr), True, (255, 255, 255))
        #screen.fill((50, 50, 50))
        #screen.blit(txt, [300, 200])
        #screen.blit(enn, [100, 400])
        move_lst=[-1,0]

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            move_lst[1]+=-1
        if key_lst[pg.K_DOWN]:
            move_lst[1]+=1
        if key_lst[pg.K_LEFT]:
            move_lst[0]+=-1
        if key_lst[pg.K_RIGHT]:
            move_lst[0]+=+2
        img_rct.move_ip(move_lst)
        screen.blit(img,img_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()