def change(x):
    return x-1

N,M=map(int,input().split())
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
answer = N*M*4
visit = [[[0]*4 for i in range(M)] for j in range(N)]
visit[start[0]][start[1]][start[2]] = 1
Que = [[start[0],start[1],start[2],0]]
while Que != []:
    i,j,d,cost = Que.pop(0)

    if cost>=answer:
        continue

    if [i,j,d] == end:
        if answer > cost:
            answer = cost
        continue

    for k in range(1,4):
        ni,nj=i+k*di[d],j+k*dj[d]
        if 0<=ni<N and 0<=nj<M and board[ni][nj] == 1:
            break
        if 0<=ni<N and 0<=nj<M and visit[ni][nj][d] == 0 and board[ni][nj] == 0:
            visit[ni][nj][d] = 1
            Que.append([ni,nj,d,cost+1])
    
    if visit[i][j][(d-1)%4] == 0:
        visit[i][j][(d-1)%4] = 1
        Que.append([i,j,(d-1)%4,cost+1])
    
    if visit[i][j][(d+1)%4] == 0:
        visit[i][j][(d+1)%4] = 1
        Que.append([i,j,(d+1)%4,cost+1])

print(answer)