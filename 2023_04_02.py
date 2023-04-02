import pygame as p
import random

p.init()

width=700
height=500

size=200

white=(255,255,255)
black=(0,0,0)

screen=p.display.set_mode((width,height))

enhance_prob=[100,97,95,93,90,87,83,80,75,72,68,65,58,50,45,40,35,28,17,5]
enhance_price=[0,100,100,300,400,500,700,900,900,1000,1000,1400,1600,2400,4000,6000,15000,25000,100000,150000]
sell_price=[1,120,150,400,500,800,1600,2300,5000,7000,10000,16000,25000,34000,50000,80000,120000,300000,500000,900000]

money=30000
enhance_number=0
run=True

while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False

        if event.type==p.MOUSEBUTTONDOWN:
            x,y=p.mouse.get_pos()
            if width/2+150<=x<=width/2+250 and height/2-50<=y<=height/2+50:
                r=random.random()
                if r<=(enhance_prob[enhance_number]/100) :
                    enhance_number+=1
                else:
                    enhance_number=0
            if width/2-250<=x<=width/2-150 and height/2-50<=y<=height/2+50:
                enhance_number=0



    image=p.image.load(str(enhance_number+1)+'.png') #webp,jpg,jpeg
    image=p.transform.scale(image,(size,size))

    
    screen.fill(white)
    screen.blit(image,(width/2-size/2,height/2-size/2))
    p.draw.circle(screen,black,(width/2+200,height/2),50,3)
    p.draw.circle(screen,black,(width/2-200,height/2),50,3)

    myFont=p.font.SysFont('arial',50,True,False)
    korean_Font=p.font.SysFont('malgungothic',36)
    print_enh=korean_Font.render("강화",True,black)
    print_sell=korean_Font.render("판매",True,black)
    print_enh_score=myFont.render("+"+str(enhance_number+1),True,black)

    screen.blit(print_enh_score,(width/2-size/2,height/2-size/2+size))
    screen.blit(print_enh,(width/2+200-37,height/2-27))
    screen.blit(print_sell,(width/2-200-37,height/2-27))

    p.display.update()

p.quit()

#https://url.kr/c2jwbn

