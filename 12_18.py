import pygame as p
import time
import random
p.init()

background=(57,200,55)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
speed=2
white=(255,255,255)
black=(0,0,0)

width=700
height=600

screen=p.display.set_mode((width,height))
size=40

positions=[[0,0,size,size],[width-size,height-size,size,size]]

run=True
bomb=random.choice([0,1])

state=0

touch=p.time.get_ticks()

while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False

    key_event=p.key.get_pressed()

    if key_event[p.K_LEFT]:
        if positions[0][0]>0:
            positions[0][0]-=speed
        else:
            positions[0][0]=width-size
            
    if key_event[p.K_RIGHT]:
        if positions[0][0]<width-size:
            positions[0][0]+=speed
        else:
            positions[0][0]=0
    if key_event[p.K_DOWN]:
        if positions[0][1]<height-size:
            positions[0][1]+=speed
        else:
            positions[0][1]=0
    if key_event[p.K_UP]:
        if positions[0][1]>0:
            positions[0][1]-=speed
        else:
            positions[0][1]=height-size


    if key_event[ord("a")]:
        if positions[1][0]>0:
            positions[1][0]-=speed
        else:
            positions[1][0]=width-size
            
    if key_event[ord("d")]:
        if positions[1][0]<width-size:
            positions[1][0]+=speed
        else:
            positions[1][0]=0
    if key_event[ord("s")]:
        if positions[1][1]<height-size:
            positions[1][1]+=speed
        else:
            positions[1][1]=0
    if key_event[ord("w")]:
        if positions[1][1]>0:
            positions[1][1]-=speed
        else:
            positions[1][1]=height-size

    screen.fill(white)

    p.draw.rect(screen,black,positions[0])
    p.draw.rect(screen,blue,positions[1])
    p.draw.rect(screen,red,positions[bomb],3)
    
    if p.time.get_ticks()-touch>300:
        state=0
    
    if state==0:
        if positions[0][0]<=positions[1][0]<=positions[0][0]+size or positions[1][0]<=positions[0][0]<=positions[1][0]+size:
            if positions[0][1]<=positions[1][1]<=positions[0][1]+size or positions[1][1]<=positions[0][1]<=positions[1][1]+size:
                bomb=(bomb+1)%2
                state=1
                touch=p.time.get_ticks()
    


    p.display.update()

p.quit()
