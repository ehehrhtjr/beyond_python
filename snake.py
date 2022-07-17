import pygame
import time
import random
import copy

pygame.init()

width=1000
height=700

speed=0.2
size=50

screen=pygame.display.set_mode((width,height))

black=(0,0,0)
yellow=(255,255,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

co_l=[black,yellow,red,blue,green]

screen.fill(green)
#    x,y,width,height
pos=[0,0,size,size]
apple_pos=[random.randrange(0,(width/size))*size
           ,random.randrange(0,(height/size))*size,size,size]


tail=0
route=[]

direction=0 # 0:right  1:down  2:left  3:up

run=True
play=True

while run:
    if play:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_ESCAPE:
                    run=False

                if event.key==pygame.K_RIGHT:
                    if direction!=2:
                        direction=0
                if event.key==pygame.K_LEFT:
                    if direction!=0:
                        direction=2
                if event.key==pygame.K_UP:
                    if direction!=1:
                        direction=3
                if event.key==pygame.K_DOWN:
                    if direction!=3:
                        direction=1

        route.append(copy.deepcopy(pos))

        time.sleep(speed)
        if direction==0:
            pos[0]+=size
        elif direction==1:
            pos[1]+=size
        elif direction==2:
            pos[0]-=size
        elif direction==3:
            pos[1]-=size

        screen.fill(green)
        pygame.draw.rect(screen,black,pos)
        pygame.draw.rect(screen,red,apple_pos)

        if tail>0:
            for i in range(tail):
                pygame.draw.rect(screen,blue,route[-(i+1)])
        pygame.display.update()

        if pos==apple_pos:
            apple_pos=[random.randrange(0,(width/size))*size
               ,random.randrange(0,(height/size))*size,size,size]
            tail+=1
        if pos[0]-size>=width or pos[0]<0:
            play=False

        if pos[1]-size>=height or pos[1]<0:
            play=False

        for i in range(tail):
            if pos==route[-(1+i)]:
                play=False
    
    else:

        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
                
                if event.key==pygame.K_RETURN:
                    play=True
                    pos=[0,0,size,size]
                    apple_pos=[random.randrange(0,(width/size))*size
                       ,random.randrange(0,(height/size))*size,size,size]
                    tail=0
                    route=[]
                    direction=0 # 0:right  1:down  2:left  3:up
        
        screen.fill(green)
        myFont=pygame.font.SysFont("arial",50,True,False)
        myFont2=pygame.font.SysFont("arial",30,False,False)
        
        score=myFont.render(str(tail),True,black)
        retry=myFont2.render('Press "ENTER" to retry',True,black)
        
        screen.blit(score,[470,300])
        screen.blit(retry,[365,350])
        pygame.display.update()
        

pygame.quit()
