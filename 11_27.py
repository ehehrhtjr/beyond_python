import pygame as p
import time
import random
p.init()

background=(57,200,55)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
speed=3
white=(255,255,255)
black=(0,0,0)

width=700
height=600

screen=p.display.set_mode((width,height))
size=40

positions=[[0,0,size,size],[width-size,height-size,size,size]]

run=True

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
        positions[0][0]+=speed
    if key_event[p.K_DOWN]:
        positions[0][1]+=speed
    if key_event[p.K_UP]:
        positions[0][1]-=speed


    screen.fill(white)

    p.draw.rect(screen,black,positions[0])
    p.display.update()

p.quit()
