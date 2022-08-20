import pygame as p

p.init()

width=700
height=700

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)

speed=2

screen=p.display.set_mode((width,height))


size=40

positions=[[0,0,size,size],[width-size,height-size,size,size]]

#positions[1][0] positions[1][1] 

#pos => positions[0]   pos2=> positions[1]
run=True

while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False

    key_event=p.key.get_pressed()
        
    
    if key_event[p.K_LEFT]:
        if positions[0][0]<0:
            positions[0][0]=width-size
        else:
            positions[0][0]-=speed
        
    if key_event[p.K_RIGHT]:
        if positions[0][0]>width-size:
            positions[0][0]=0
        else:
            positions[0][0]+=speed
        
    if key_event[p.K_DOWN]:
        if positions[0][1]>height-size:
            positions[0][1]=0
        else:
            positions[0][1]+=speed
        
    if key_event[p.K_UP]:
        if positions[0][1]<0:
            positions[0][1]=height-size
        else:
            positions[0][1]-=speed
    
    
    if key_event[ord("a")]:
        if positions[1][0]<0:
            positions[1][0]=width-size
        else:
            positions[1][0]-=speed
        
    if key_event[ord("d")]:
        if positions[1][0]>width-size:
            positions[1][0]=0
        else:
            positions[1][0]+=speed
        
    if key_event[ord("s")]:
        if positions[1][1]>height-size:
            positions[1][1]=0
        else:
            positions[1][1]+=speed
        
    if key_event[ord("w")]:
        if positions[1][1]<0:
            positions[1][1]=height-size
        else:
            positions[1][1]-=speed

    screen.fill(black)
    
    p.draw.rect(screen,blue,positions[1])
    p.draw.rect(screen,white,positions[0])
    #p.draw.rect(screen,(255,0,0),positions[1],3)
    
    
    if positions[0][0]<=positions[1][0]<=positions[0][0]+size or positions[1][0]<=positions[0][0]<=positions[1][0]+size:
        if positions[0][1]<=positions[1][1]<=positions[0][1]+size or positions[1][1]<=positions[0][1]<=positions[1][1]+size:
            
            p.draw.rect(screen,red,positions[0])
            p.draw.rect(screen,red,positions[1])
    
    p.display.update()
p.quit()
