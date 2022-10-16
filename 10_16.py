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
                if position[0]<400:
                    position[0]+=50
                else:
                    position[0]=0
            
            if event.key==pygame.K_UP:
                if position[1]>0:
                    position[1]-=50
                else:
                    position[1]=400
                
            if event.key==pygame.K_LEFT:
                if position[0]>0:
                    position[0]-=50
                else:
                    position[0]=400
                    
            if event.key==pygame.K_DOWN:
                if position[1]<400:
                    position[1]+=50
                else:
                    position[1]=0
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),position)
    pygame.display.update()

pygame.quit()
