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

snake_pos=[0,0,size,size]
apple_pos=[random.randrange(width/size)*size,
          random.randrange(height/size)*size,size,size]

direction=0 # 0: 오른 | 1: 아래 | 2: 왼 | 3: 위

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if direction!=2:
                    direction=0
            if event.key==pygame.K_DOWN:
                if direction!=3:
                    direction=1
            if event.key==pygame.K_LEFT:
                if direction!=0:
                    direction=2
            if event.key==pygame.K_UP:
                if direction!=1:
                    direction=3
             
    time.sleep(speed)
    if direction==0:
        if snake_pos[0]<width-size:
            snake_pos[0]+=size
    if direction==1:
        if snake_pos[1]<height-size:
            snake_pos[1]+=size
    if direction==2:
        if snake_pos[0]>0:
            snake_pos[0]-=size
    if direction==3:
        if snake_pos[1]>0:
            snake_pos[1]-=size

    if snake_pos==apple_pos: # 사과를 먹었을 때
        apple_pos=[random.randrange(width/size)*size,
          random.randrange(height/size)*size,size,size]

    screen.fill(green)
    pygame.draw.rect(screen,red,apple_pos)
    pygame.draw.rect(screen,black,snake_pos)
    pygame.display.update()
pygame.quit()
