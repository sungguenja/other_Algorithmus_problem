from copy import deepcopy
direction = [[0,1],[1,0],[0,-1],[-1,0]]

N,M=map(int,input().split())
sea = [0]*N
ice=0
for i in range(N):
    horizon = []
    horizon = list(map(int,input().split()))
    sea[i] = horizon[:]

day = 0
ice = 0
while ice < 2:
    ice = 0
    copy_sea = deepcopy(sea)
    for i in range(N):
        for j in range(M):
            if copy_sea[i][j] != 0:
                for k in direction:
                    ni=i+k[0]
                    nj=j+k[1]
                    if 0<=ni<N and 0<=nj<M:
                        if copy_sea[i][j] != 0 and sea[ni][nj] == 0:
                            copy_sea[i][j] -= 1
    
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if copy_sea[i][j] != 0 and visit[i][j] == 0:
                que = [[i,j]]
                visit[i][j] = 1
                while que != []:
                    X = que.pop(0)
                    y,x=X[0],X[1]
                    for k in direction:
                        ni=y+k[0]
                        nj=x+k[1]
                        if 0<=ni<N and 0<=nj<M:
                            if copy_sea[ni][nj] != 0 and visit[ni][nj] == 0:
                                que.append([ni,nj])
                                visit[ni][nj] = 1
                ice += 1
    day += 1
    if copy_sea == sea or copy_sea == [[0]*M]*N:
        day = 0
        ice = 2
    sea = deepcopy(copy_sea)
print(day)