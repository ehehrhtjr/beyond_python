import pygame
import random

pygame.init()

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

money=30000

enhance_prob=[0.95,0.93,0.9,0.87,0.85,0.85, 0.85,0.8,0.77,0,75,0.75,0.73,0.7,0.6,0.57,0.5,0.5,0.4,0.35]
 #              1    2    3   4    5   6     7    8   9    10   11   12   13  14   15  16  17  18  19
ehance_price=   [0,100, 100, 300, 400,500,700, 900, 900,1000,1000,1400,1600,2400,4000,6000,15000,25000,100000 ]
sell_price= [0,100, 100, 200, 500,700,800, 800, 1000,1500,3000,5000,8000,10000,20000,25000,50000,50000,70000]
    
    
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if width/2+150<=x<=width/2+250 and height/2-50<=y<=height/2+50:
                random_number=random.random()
                
                if random_number<=enhance_prob[image_number-1]:
                    if image_number<20:
                        image_number+=1
                        gun_image=pygame.image.load('gun'+str(image_number)+'.png')
                        gun_image=pygame.transform.scale(gun_image,(size,size))
                else:
                    image_number=1
                    gun_image=pygame.image.load('gun'+str(image_number)+'.png')
                    gun_image=pygame.transform.scale(gun_image,(size,size))

            if width/2-250<=x<=width/2-150 and height/2-50<=y<=height/2+50:
                print("success")
    myFont=pygame.font.SysFont('arial',50,True,False)
    korean_Font=pygame.font.SysFont("malgungothic",36)
    
    enhance_score=myFont.render("+"+str(image_number),True,black)
    enhance_prob_print=myFont.render(str(enhance_prob[image_number-1]*100)+"%",True,black)
    print_enh=korean_Font.render("강화",True,black)
    print_sell=korean_Font.render("판매",True,black)
    
    screen.fill(white)
    screen.blit(gun_image,(width/2-size/2,height/2-size/2))
    pygame.draw.circle(screen,black,(width/2+200,height/2),50,3)
    pygame.draw.circle(screen,black,(width/2-200,height/2),50,3)
    
    screen.blit(enhance_score,[width/2-size/2,height/2-size/2+size])
    screen.blit(enhance_prob_print,[width/2-size/2+60,height/2-size/2+size+60])
    screen.blit(print_enh,(width/2+200-37,height/2-27))
    screen.blit(print_sell,(width/2-200-37,height/2-27))
    
    pygame.display.update()

pygame.quit()
