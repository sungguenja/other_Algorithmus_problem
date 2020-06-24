from copy import deepcopy
N=int(input())
answer = 0
def solution(cnt,board,size,score):
    global answer
    if cnt>=5:
        return
    
    if score>answer:
        answer = score
    
    for i in range(4):
        copy_board = deepcopy(board)
        moving(copy_board,i,size)
        print(cnt,answer,board)
        if copy_board == board:
            continue
        else:
            now_score = 0
            for j in range(size):
                now_score = max(now_score,max(copy_board[j]))
            solution(cnt+1,copy_board,size,now_score)

def moving(moving_board,way,magino):
    if way==0:
        for i in range(magino):
            for j in range(magino-1,-1,-1):
                if moving_board[i][j] != 0:
                    k=j+1
                    while 0<=k<magino and moving_board[i][k] != 0:
                        k+=1
                    if k==magino:
                        k-=1
                    if 0<=k<magino:
                        if k!=j and moving_board[i][k] == 0:
                            moving_board[i][j],moving_board[i][k]=moving_board[i][k],moving_board[i][j]
                        elif k!=j and moving_board[i][j] == moving_board[i][k]:
                            moving_board[i][j] = 0
                            moving_board[i][k] *= 2
                        elif k!=j and moving_board[i][j] != moving_board[i][k]:
                            k-=1
                            if 0<=k and k!=j:
                                moving_board[i][j],moving_board[i][k]=moving_board[i][k],moving_board[i][j] 
    elif way==1:
        for j in range(magino):
            for i in range(magino-1,-1,-1):
                if moving_board[i][j] != 0:
                    k=i
                    while 0<=k<magino and moving_board[k][j] != 0:
                        k+=1
                    if k==magino:
                        k-=1
                    if 0<=k<magino:
                        if k!=i and moving_board[k][j] == 0:
                            moving_board[k][j], moving_board[i][j] = moving_board[i][j], moving_board[k][j]
                        elif k!=i and moving_board[k][j] == moving_board[i][j]:
                            moving_board[i][j] = 0
                            moving_board[k][j] *= 2
                        elif k!=j and moving_board[k][j] != moving_board[i][j]:
                            k-=1
                            if 0<=k<magino and k!=i:
                                moving_board[i][j],moving_board[k][j] =  moving_board[k][j],moving_board[i][j]
    elif way==2:
        for i in range(magino):
            for j in range(magino):
                if moving_board[i][j] != 0:
                    k=j-1
                    while 0<=k<magino and moving_board[i][k] != 0:
                        k-=1
                    if k==-1:
                        k+=1
                    if 0<=k<magino:
                        if k!=j and moving_board[i][k] == 0:
                            moving_board[i][j],moving_board[i][k]=moving_board[i][k],moving_board[i][j]
                        elif k!=j and moving_board[i][j] == moving_board[i][k]:
                            moving_board[i][j] = 0
                            moving_board[i][k] *= 2
                        elif k!=j and moving_board[i][j] != moving_board[i][k]:
                            k+=1
                            if k<magino and k!=j:
                                moving_board[i][j],moving_board[i][k]=moving_board[i][k],moving_board[i][j] 
    elif way==3:
        for j in range(magino):
            for i in range(magino-1,-1,-1):
                if moving_board[i][j] != 0:
                    k=i
                    while 0<=k<magino and moving_board[k][j] != 0:
                        k-=1
                    if k==-1:
                        k+=1
                    if 0<=k<magino:
                        if k!=i and moving_board[k][j] == 0:
                            moving_board[k][j], moving_board[i][j] = moving_board[i][j], moving_board[k][j]
                        elif k!=i and moving_board[k][j] == moving_board[i][j]:
                            moving_board[i][j] = 0
                            moving_board[k][j] *= 2
                        elif k!=j and moving_board[k][j] != moving_board[i][j]:
                            k+=1
                            if 0<=k<magino and k!=i:
                                moving_board[i][j],moving_board[k][j] = moving_board[k][j],moving_board[i][j]

game = [0]*N
for i in range(N):
    game[i] = list(map(int,input().split()))

solution(0,game,N,0)
print(answer)