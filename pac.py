import pygame as p
import random
import time

class pacman:
    def __init__(self,direction,x,y):
        self.direction=direction
        self.x=x
        self.y=y
        
    

    def move(self,m):
        if self.direction==0:
            if m[self.y][self.x+1]!=0:
                self.x+=1
        if self.direction==1:
            if m[self.y+1][self.x]!=0:
                self.y+=1
        if self.direction==2:
            if m[self.y][self.x-1]!=0:
                self.x-=1
        if self.direction==3:
            if m[self.y-1][self.x]!=0:
                self.y-=1



class ghost_boss:
    def __init__(self):
        self.x=18
        self.y=5
        
        
    def follow(self,pacman,matrix):
        N, M = pacman.x,pacman.y
        
        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
                # 좌/우/위/아래 방향 이동
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

                # BFS 경로 탐색
                # queue 방식 사용
        queue = [(self.y,self.x)]
        visited[self.y][self.x] = 1
        cnt=0
        while queue:
            y, x = queue.pop(0)
            
            if x == N and y == M:
                print(visited[M][N])
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix):
                    if visited[ny][nx] == 0 and matrix[ny][nx] != 0:
        #######################################################################################################
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny,nx))
            
        queue=[(M,N)]
        stack  =[(M,N)]
        while queue:
            y,x=queue.pop(0)

            if x==self.x and y==self.y:
                print("finish")
                break
                

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix):
                    if visited[y][x]-visited[ny][nx]==1:
                        stack.append((ny,nx))
                        queue.append((ny,nx))
                        break
        stack.pop()
        self.y,self.x=stack.pop()
            
        
        

p.init()

black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

width=400
height=140

screen=p.display.set_mode((width,height))


matrix=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ,[0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0]
       ,[0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0]
       ,[0,1,0,2,1,0,1,1,1,1,1,1,1,1,0,1,2,0,1,0]
       ,[0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0]
       ,[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
       ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

pa=pacman(0,1,1)
g_b=ghost_boss()



bgColor=(0,0,0)
wall=(0,0,255)
pac=(255,255,0)

screen.fill(bgColor)
  
speed=1.0
size=20

state=True
route=[]
run=True
while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
        
        if event.type==p.KEYDOWN:
            if event.key==p.K_ESCAPE:
                run=False
            # 0 : right 1:down 2:left 3:up
            if event.key==p.K_RIGHT:
                pa.direction=0
            elif event.key==p.K_DOWN:
                pa.direction=1
            elif event.key==p.K_LEFT:
                pa.direction=2
            elif event.key==p.K_UP:
                pa.direction=3
    

    time.sleep(speed)
    screen.fill(bgColor)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                p.draw.rect(screen,wall,[j*size,i*size,size,size])
    
    p.draw.rect(screen,red,[g_b.x*size,g_b.y*size,size,size])
    p.draw.rect(screen,pac,[pa.x*size,pa.y*size,size,size])
    p.display.update()
            
    pa.move(matrix)
    g_b.follow(pa,matrix)
        
                    
p.quit()
