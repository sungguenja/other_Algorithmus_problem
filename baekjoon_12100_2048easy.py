from copy import deepcopy
N=int(input())
answer = 0
def solution(cnt,board,size,score):
    global answer
    if cnt>5:
        return
    
    if score>answer:
        answer = score

    if cnt<5:
        for i in range(4):
            copy_board = deepcopy(board)
            moving(copy_board,i,size)
            if copy_board != board:
                now_score = 0
                for j in range(size):
                    now_score = max(now_score,max(copy_board[j]))
                solution(cnt+1,copy_board,size,now_score)

def moving(moving_board,way,magino):
    trigger = [[False]*magino for _ in range(magino)]
    # 한번 합쳐지고 더 합쳐지면 안된다
    if way==0:
        for i in range(magino):
            for j in range(magino-2,-1,-1):
                if moving_board[i][j] != 0:
                    k=j+1
                    while 0<=k<magino and moving_board[i][k] == 0:
                        k+=1
                    if k==magino:
                        moving_board[i][magino-1] = moving_board[i][j]
                        moving_board[i][j] = 0
                    elif 0<=k<magino:
                        if moving_board[i][j] == moving_board[i][k] and not trigger[i][k]:
                            moving_board[i][k] *= 2
                            moving_board[i][j] = 0
                            trigger[i][k] = True
                        else:
                            moving_board[i][j],moving_board[i][k-1] = moving_board[i][k-1],moving_board[i][j]
    elif way==1:
        for j in range(magino):
            for i in range(magino-2,-1,-1):
                if moving_board[i][j] != 0:
                    k=i+1
                    while 0<=k<magino and moving_board[k][j] == 0:
                        k+=1
                    if k==magino:
                        moving_board[magino-1][j] = moving_board[i][j]
                        moving_board[i][j] = 0
                    elif 0<=k<magino:
                        if moving_board[i][j] == moving_board[k][j] and not trigger[k][j]:
                            moving_board[k][j] *= 2
                            moving_board[i][j] = 0
                            trigger[k][j] = True
                        else:
                            moving_board[i][j],moving_board[k-1][j] = moving_board[k-1][j],moving_board[i][j]
    elif way==2:
        for i in range(magino):
            for j in range(1,magino):
                if moving_board[i][j] != 0:
                    k=j-1
                    while 0<=k<magino and moving_board[i][k] == 0:
                        k-=1
                    if k==-1:
                        moving_board[i][0] = moving_board[i][j]
                        moving_board[i][j] = 0
                    elif 0<=k<magino:
                        if moving_board[i][j] == moving_board[i][k] and not trigger[i][k]:
                            moving_board[i][k] *= 2
                            moving_board[i][j] = 0
                            trigger[i][k] = True
                        else:
                            moving_board[i][j],moving_board[i][k+1] = moving_board[i][k+1],moving_board[i][j]
    elif way==3:
        for j in range(magino):
            for i in range(1,magino):
                if moving_board[i][j] != 0:
                    k=i-1
                    while 0<=k<magino and moving_board[k][j] == 0:
                        k-=1
                    if k==-1:
                        moving_board[0][j] = moving_board[i][j]
                        moving_board[i][j] = 0
                    elif 0<=k<magino:
                        if moving_board[i][j] == moving_board[k][j] and not trigger[k][j]:
                            moving_board[k][j] *= 2
                            moving_board[i][j] = 0
                            trigger[k][j] = True
                        else:
                            moving_board[i][j],moving_board[k+1][j] = moving_board[k+1][j],moving_board[i][j]

game = [0]*N
for i in range(N):
    game[i] = list(map(int,input().split()))

solution(0,game,N,0)
if N==1:
    answer = game[0][0]
print(answer)