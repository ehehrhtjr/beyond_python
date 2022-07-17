import pygame as p

def draw_x(x,y):
    p.draw.line(screen,red,[x,y],[x+100,y+100],10)
    p.draw.line(screen,red,[x+100,y],[x,y+100],10)
    
def check_win(mat,c_y,c_x,h,turn,c):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    
    visited = [[0]*c for _ in range(c)]
    queue = []#
    visited[c_y][c_x] = 1
    
    cnt=1
    w=False
    
    for i in range(8):#
        queue.append((c_y,c_x))#
        if cnt==h:
            w=True
            break
        if i%2==0:
            cnt=1
        
        while queue:#
            y, x = queue.pop(0)#

            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < c:
                if visited[ny][nx] == 0 and mat[ny][nx]==turn:
                    visited[ny][nx] = 1
                    cnt+=1
                    queue.append((ny,nx))
    for i in mat:
        print(i)
        
    print(cnt)
    return w


    
    '''
    for i in range(c):
        state_win=True
        for j in range(c):
            if mat[i][j]!=turn:
                state_win=False
        if state_win:
            return True
        
    for i in range(c):
        state_win=True
        for j in range(c):
            if mat[j][i]!=turn:
                state_win=False
            
        if state_win:
            return True
    
    state_win=True
    for i in range(c):
        if mat[i][i]!=turn:
            state_win=False
    if state_win:
        return True
    
    state_win=True
    for i in range(c):
        if mat[i][2-i]!=turn:
            state_win=False
    if state_win:
        return True
    '''
    

size=100
cell=8
hit=5

matrix=[[0]*cell for i in range(cell)]

width=size*cell
height=size*cell

screen=p.display.set_mode((width,height))

white=(255,255,255) #다 컴마임
black=(0,0,0)#다 컴마임
blue=(0,0,255)#다 컴마임
red=(255,0,0)#다 컴마임

screen.fill(white)

run=True

turn=0

for i in range(cell):
    for j in range(cell):
        p.draw.rect(screen,black,[j*100,i*100,size,size],2)


# dot(점)  |  comma(쉼표)
while run:
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
        
        if event.type==p.MOUSEBUTTONDOWN:
            x,y=p.mouse.get_pos()# 컴마 = 닷
            if turn==0:
                for i in range(cell):
                    for j in range(cell):
                        if size*j<x<size*(j+1) and size*i<y<size*(i+1):
                            if matrix[i][j]==0:
                                p.draw.circle(screen,blue,[(size/2)+size*j,(size/2)+size*i],size/2,5)
                                matrix[i][j]=1
                                result=check_win(matrix,i,j,hit,1,cell)
                                if result:
                                    print("player 1 win")
                                turn=1
            else:
                for i in range(cell):
                    for j in range(cell):
                        if size*j<x<size*(j+1) and size*i<y<size*(i+1):
                            if matrix[i][j]==0:
                                draw_x(j*size,i*size)
                                matrix[i][j]=2
                                result=check_win(matrix,i,j,hit,2,cell)
                                if result:
                                    print("player 2 win")
                                turn=0
             #   dot |  컴마
    p.display.update()

p.quit()
            
