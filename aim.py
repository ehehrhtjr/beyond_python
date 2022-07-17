import pygame as p
import random
import time
width=1000
height=750

p.init()

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
white=(255,255,255)

screen=p.display.set_mode((width,height))

screen.fill(white)

run=True

size=100


r_x=random.randrange(width-size)
r_y=random.randrange(height-size)

score=0
start=time.time()
play=True
high_score=0

while run:
    if play:
        x,y=p.mouse.get_pos()

        for event in p.event.get():
            if event.type==p.QUIT:
                run=False

            if event.type==p.MOUSEBUTTONDOWN:

                if r_x<=x<=r_x+size and r_y<=y<=r_y+size:
                    score+=100
                    r_x=random.randrange(width-size)
                    r_y=random.randrange(height-size)

        end=time.time()
        current_time=end-start

        if current_time>30:
            play=False
            if high_score<score:
                high_score=score

        p.mouse.set_visible(False)
        screen.fill(white)

        p.draw.rect(screen,black,[r_x,r_y,size,size])
        p.draw.line(screen,red,[x-15,y],[x-5,y])
        p.draw.line(screen,red,[x+15,y],[x+5,y])
        p.draw.line(screen,red,[x,y-15],[x,y-5])
        p.draw.line(screen,red,[x,y+15],[x,y+5])
        p.draw.circle(screen,red,[x,y],10,1)
        p.draw.circle(screen,red,[x,y],3)

        myfont=p.font.SysFont("arial",50,True,False)
        myfont2=p.font.SysFont("arial",30,True,False)

        score_print=myfont.render(str(score),True,black)
        time_print=myfont2.render(str(round(30-current_time,2)),True,black)

        screen.blit(score_print,[900,0])
        screen.blit(time_print,[900,100])
        p.display.update()
        
        
    else:
        time.sleep(0.1)
        for event in p.event.get():
            if event.type==p.QUIT:
                run=False

            if event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    run=False
                if event.key==p.K_RETURN:
                    play=True
                    r_x=random.randrange(width-size)
                    r_y=random.randrange(height-size)
                    score=0
                    start=time.time()
                    
        screen.fill(white)
        myfont=p.font.SysFont("arial",50,True,False)
        retry=myfont.render("Press ENTER to Retry",True,black)
        screen.blit(retry,[300,500])
        score_print=myfont.render(str(score),True,black)
        high_score_print=myfont.render(str(high_score),True,black)#
        screen.blit(high_score_print,[500,150])#
        screen.blit(score_print,[500,400])
        p.display.update()
        
        
    
p.quit()
