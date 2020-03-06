direction = [[-1,0],[0,-1],[1,0],[0,1]]

N=int(input())
aqua = []
fish = []
for i in range(N):
    horizon=[]
    horizon=list(map(int,input().split()))
    for j in range(N):
        if 0<horizon[j]<9:
            fish.append([i,j])
        elif horizon[j]==9:
            shark = [i,j]
    aqua.append(horizon)

t=0
eat=0
big=2
que=[[shark[0],shark[1],0,9]]
visit =[[0]*N for _ in range(N)]
aqua[que[0][0]][que[0][1]]=0
d=0
while que != []:
    X=que.pop(0)
    i,j,d,size=X[0],X[1],X[2],X[3]
    for k in direction:
        ni=i+k[0]
        nj=j+k[1]
        if 0<=ni<N and 0<=nj<N and visit[ni][nj]==0:
            if aqua[ni][nj] <= big or aqua[ni][nj] == 9:
                if aqua[ni][nj] == 0 or aqua[ni][nj] == big:
                    visit[ni][nj]=1
                    que.append([ni,nj,d+1,0])
                elif 0<aqua[ni][nj]<big:
                    visit[ni][nj]=1
                    que.append([ni,nj,d+1,aqua[ni][nj]])
print(t)