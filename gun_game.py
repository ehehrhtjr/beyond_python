import pygame

width=700
height=500

size=200

white=(255,255,255)
black=(0,0,0)
screen=pygame.display.set_mode((width,height))

gun_image=pygame.image.load('gun1.png')
gun_image=pygame.transform.scale(gun_image,(size,size))

run=True

image_number=1
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
                
    screen.fill(white)
    screen.blit(gun_image,(width/2-size/2,height/2-size/2))
    pygame.draw.circle(screen,black,(width/2+200,height/2),50)
    pygame.display.update()

pygame.quit()
            
