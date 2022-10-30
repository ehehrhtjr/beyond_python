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

direction=0 # 0: 오른 | 1: 아래 | 2: 왼 | 3: 위

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                direction=0
            if event.key==pygame.K_DOWN:
                direction=1
            if event.key==pygame.K_LEFT:
                direction=2
            if event.key==pygame.K_UP:
                direction=3
             
    time.sleep(speed)
    if direction==0:
        snake_pos[0]+=size
    if direction==1:
        snake_pos[1]+=size
    if direction==2:
        snake_pos[0]-=size
    if direction==3:
        snake_pos[1]-=size

    screen.fill(green)
    pygame.draw.rect(screen,black,snake_pos)
    pygame.display.update()
pygame.quit()
