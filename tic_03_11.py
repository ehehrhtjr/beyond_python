import pygame as p

p.init()

c=3
size=100

width=size*c
height=size*c

screen=p.display.set_mode((width,height))

white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)

screen.fill(white)


for j in range(c):
    for i in range(c):
        p.draw.rect(screen,black,[i*size,j*size,size,size],1)

p.display.update()    
run=True

while run:
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
        
        if event.type==p.MOUSEBUTTONDOWN:
            x,y=p.mouse.get_pos()

            for j in range(c):
                for i in range(c):
                    if i*size<x<i*size+size and j*size<y<j*size+size:
                        #p.draw.rect(screen,black,[i,j,size,size])
                        p.draw.circle(screen,blue,[i*size+size/2,j*size+size/2],size/2,5)

                        #         색 , 위치(중점), 반지름, 테두리
    p.display.update()
p.quit()

