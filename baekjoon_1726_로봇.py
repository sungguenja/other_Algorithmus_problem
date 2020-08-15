def change(x):
    return x-1

N,M=map(int,input().split())
answer = N*M*4
di = [0,1,0,-1]
dj = [1,0,-1,0]
board = [list(map(int,input().split())) for _ in range(N)]
start = list(map(change,map(int,input().split())))
if start[2] == 1:
    start[2] = 2
elif start[2] == 2:
    start[2] = 1
end = list(map(change,map(int,input().split())))
if end[2] == 1:
    end[2] = 2
elif end[2] == 2:
    end[2] = 1
visit = [[[0]*4 for i in range(M)] for j in range(N)]
visit[start[0]][start[1]][start[2]] = 1

def solution(i,j,d,cost=0):
    global answer
    if cost>=answer:
        return
    
    if [i,j,d] == end:
        if cost<answer:
            answer = cost
        return
    
    for k in range(1,4):
        ni,nj=i+k*di[d],j+k*dj[d]
        if 0<=ni<N and 0<=nj<M and board[ni][nj] == 1:
            break
        if 0<=ni<N and 0<=nj<M and visit[ni][nj][d] == 0 and board[ni][nj] == 0:
            visit[ni][nj][d] = 1
            solution(ni,nj,d,cost+1)
            visit[ni][nj][d] = 0

    if visit[i][j][(d-1)%4] == 0:
        visit[i][j][(d-1)%4] = 1
        solution(i,j,(d-1)%4,cost+1)
        visit[i][j][(d-1)%4] = 0
    
    if visit[i][j][(d+1)%4] == 0:
        visit[i][j][(d+1)%4] = 1
        solution(i,j,(d+1)%4,cost+1)
        visit[i][j][(d+1)%4] = 0
    

solution(start[0],start[1],start[2])
print(answer)