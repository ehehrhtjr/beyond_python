import pygame as p

p.init()

width=700
height=700

screen=p.display.set_mode((width,height))


size=40
pos=[0,0,size,size]

run=True

while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False

    key_event=p.key.get_pressed()
        
    
    if key_event[p.K_LEFT]:
        pos[0]-=1
        
    if key_event[p.K_RIGHT]:
        pos[0]+=1
        
    if key_event[p.K_DOWN]:
        pos[1]+=1
        
    if key_event[p.K_UP]:
        pos[1]-=1

    screen.fill((0,0,0))
    p.draw.rect(screen,(255,255,255),pos)
    p.display.update()
p.quit()
