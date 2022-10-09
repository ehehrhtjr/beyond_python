import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
run=True

position=[0,0,100,100]


while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                position[0]+=50
            if event.key==pygame.K_UP:
                position[1]-=50
            if event.key==pygame.K_LEFT:
                position[0]-=50
            if event.key==pygame.K_DOWN:
                position[1]+=50
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),position)
    pygame.display.update()

pygame.quit()
