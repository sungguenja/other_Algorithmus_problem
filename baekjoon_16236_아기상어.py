direction = [[-1,0],[0,-1],[0,1],[1,0]]

N=int(input())
aqua = []
fish = []
for i in range(N):
    horizon=[]
    horizon=list(map(int,input().split()))
    for j in range(N):
        if horizon[j]==9:
            shark = [i,j]
            break
    aqua.append(horizon)

t=0
eat=0
big=2
que=[[shark[0],shark[1],0,0,5]]
visit =[[0]*N for _ in range(N)]
aqua[que[0][0]][que[0][1]]=0
visit[que[0][0]][que[0][1]]=1
d=0
while que != []:
    X=que.pop(0)
    i,j,d,size,goal=X[0],X[1],X[2],X[3],X[4]
    trigger = False
    if size!=0:
        que = [[i,j,0,0,5]]
        visit =[[0]*N for _ in range(N)]
        aqua[i][j] = 0
        visit[i][j] = 1
        t+=d
        eat+=1
        if eat == big:
            big+=1
            eat=0
    else:
        for k in range(4):
            ni=i+direction[k][0]
            nj=j+direction[k][1]
            if goal == 1 and k == 3:
                for point in range(len(que)):
                    if nj+1<N and que[point][0] == ni and que[point][1] == nj+1:
                        trigger = True
                        break
            elif goal == 2 and k == 3:
                for point in range(len(que)):
                    if nj-1>0 and que[point][0] == ni and que[point][1] == nj-1:
                        trigger = True
                        break
            if trigger:
                trigger = False
                break
            if 0<=ni<N and 0<=nj<N and visit[ni][nj]==0:
                if aqua[ni][nj] <= big:
                    if aqua[ni][nj] == 0 or aqua[ni][nj] == big:
                        visit[ni][nj]=1
                        que.append([ni,nj,d+1,0,k])
                    elif 0<aqua[ni][nj]<big:
                        visit[ni][nj]=1
                        que.append([ni,nj,d+1,aqua[ni][nj],k])
print(t)