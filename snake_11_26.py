import pygame
import random

pygame.init()
screen=pygame.display.set_mode((400,400))

run=True
position=[0,0,50,50]
direction=0 # 0:오른쪽, 1:아래, 2:왼쪽, 3:위쪽

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                direction=0
            if event.key==pygame.K_LEFT: #K_UP , K_DOWN
                direction=2
            if event.key==pygame.K_DOWN:
                direction=1
            if event.key==pygame.K_UP: #K_UP , K_DOWN
                direction=3
    if direction==0:
        if position[0]<350:
            position[0]+=10
    if direction==2:
        if position[0]>0:
            position[0]-=10
    if direction==1:
        if position[1]<350:
            position[1]+=10
    if direction==3: 
        if position[1]>0:
            position[1]-=10


    screen.fill((255,255,255))
    pygame.time.wait(100)

    pygame.draw.rect(screen,(255,0,0),position)
    #                         색      (x,y,width,height) 크기
    
    pygame.display.update()

pygame.quit()
