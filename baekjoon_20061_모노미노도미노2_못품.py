N = int(input())
blocks = [list(map(int,input().split())) for i in range(N)]

green = [[0]*4 for i in range(4)]
blue = [[0]*4 for i in range(4)]

score = 0

for block in blocks:
    t,x,y = block
    # 1은 점 2는 ㅡ 3은 | x가 행 y가 열
    if t==1:
        x2,y2=x,y
    elif t==2:
        x2,y2=x,y+1
    else:
        x2,y2=x+1,y
    
    for k in range(5):
        if k==4:
            break
        if green[k][y]==1 or green[k][y2]==1:
            break
    if k==0:
        for tt in range(3,0,-1):
            green[tt] = green[tt-1][:]
        green[0] = [0]*4
        green[0][y] = 1
        green[0][y2] = 1
    else:
        green[k-1][y] = 1
        green[k-1][y2] = 1
        if t == 3:
            if k-2>=0:
                green[k-2][y] = 1
            else:
                for tt in range(3,0,-1):
                    green[tt] = green[tt-1][:]
                green[0] = [0]*4
                green[0][y] = 1
                green[0][y2] = 1
        
        for ty in range(4):
            if green[ty] == [1]*4:
                score += 1
                for tt in range(ty,0,-1):
                    green[tt] = green[tt-1][:]
                green[0] = [0]*4

    for k in range(5):
        if k==4:
            break
        if blue[x][k]==1 or blue[x2][k]==1:
            break
    
    if k==0:
        for tt in range(3,0,-1):
            for cx in range(4):
                blue[cx][tt] = blue[cx][tt-1]
        for cx in range(4):
            if cx == x or cx == x2:
                blue[cx][0] = 1
            else:
                blue[cx][0] = 0
    else:
        blue[x][k-1] = 1
        blue[x2][k-1] = 1
        if t == 2:
            if k-2>=0:
                blue[x][k-2] = 1
                blue[x2][k-1] = 1
            else:
                for tt in range(3,0,-1):
                    for cx in range(4):
                        blue[cx][tt] = blue[cx][tt-1]
                for cx in range(4):
                    if cx == x or cx == x2:
                        blue[cx][0] = 1
                    else:
                        blue[cx][0] = 0
            
        for ty in range(4):
            for tx in range(4):
                if blue[tx][ty] == 0:
                    break
            else:
                score += 1
                for tt in range(tx,0,-1):
                    for cx in range(4):
                        blue[cx][tt] = blue[cx][tt-1]
                for cx in range(4):
                    blue[cx][0] = 0

block_cnt = 0
for i in range(4):
    for j in range(4):
        if green[i][j] == 1:
            block_cnt += 1
        if blue[i][j] == 1:
            block_cnt += 1

print(score)
print(block_cnt)