from itertools import combinations
direction = [[0,1],[1,0],[0,-1],[-1,0]]

N,M,G,R = map(int,input().split())
splash=[]
garden = [0]*N
for i in range(N):
    horizon = []
    horizon = list(map(int,input().split()))
    for j in range(M):
        if horizon[j] == 2:
            splash.append([i,j])
    garden[i] = horizon[:]
case = []
for i in range(1<<len(splash)):
    casing = []
    if bin(i).count('1') != G+R:
        continue
    for j in range(len(splash)):
        if i&(1<<j):
            casing.append(splash[j])
    case.append(casing)

maximun_flower = -1
while case != []:
    X = case.pop()
    X_case = list(combinations(X,G))
    for c in X_case:
        G_case=c
        R_case=[]
        for k in X:
            if k not in G_case:
                R_case.append(k)
        visit = [[0]*M for _ in range(N)]
        que = []
        for i in G_case:
            visit[i[0]][i[1]] = ['G',0]
            que.append([i[0],i[1]])
        for i in R_case:
            visit[i[0]][i[1]] = ['R',0]
            que.append([i[0],i[1]])
        while que != []:
            now = que.pop(0)
            i,j=now[0],now[1]
            for k in direction:
                ni=i+k[0]
                nj=j+k[1]
                if 0<=ni<N and 0<=nj<M:
                    if garden[ni][nj] != 0:
                        if visit[ni][nj] == 0:
                            visit[ni][nj] = [visit[i][j][0],visit[i][j][1]+1]
                            que.append([ni,nj])
                        else:
                            if type(visit[ni][nj])==list and visit[ni][nj][0] != visit[i][j][0] and visit[ni][nj][1] == visit[i][j][1]+1:
                                visit[ni][nj] = 'Flower'
                                if [ni,nj] in que:
                                    que.pop(que.index([ni,nj]))
                                
        flower = 0
        for i in range(N):
            for j in range(M):
                if visit[i][j] == 'Flower':
                    flower += 1
        if maximun_flower<flower:
            maximun_flower=flower


print(maximun_flower)