import pygame as p

p.init()

width=700
height=700

screen=p.display.set_mode((width,height))


size=40
pos=[0,0,size,size]
pos2=[width-size,height-size,size,size]

run=True

while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False

    key_event=p.key.get_pressed()
        
    
    if key_event[p.K_LEFT]:
        if pos[0]<0:
            pos[0]=width-size
        else:
            pos[0]-=1
        
    if key_event[p.K_RIGHT]:
        if pos[0]>width-size:
            pos[0]=0
        else:
            pos[0]+=1
        
    if key_event[p.K_DOWN]:
        if pos[1]>height-size:
            pos[1]=0
        else:
            pos[1]+=1
        
    if key_event[p.K_UP]:
        if pos[1]<0:
            pos[1]=height-size
        else:
            pos[1]-=1
    
    
    if key_event[ord("a")]:
        if pos2[0]<0:
            pos2[0]=width-size
        else:
            pos2[0]-=1
        
    if key_event[ord("d")]:
        if pos2[0]>width-size:
            pos2[0]=0
        else:
            pos2[0]+=1
        
    if key_event[ord("s")]:
        if pos2[1]>height-size:
            pos2[1]=0
        else:
            pos2[1]+=1
        
    if key_event[ord("w")]:
        if pos2[1]<0:
            pos2[1]=height-size
        else:
            pos2[1]-=1

    screen.fill((0,0,0))
    
    p.draw.rect(screen,(0,0,255),pos2)
    p.draw.rect(screen,(255,255,255),pos)
    
    

    p.display.update()
p.quit()
