direction = [[0,1],[1,0],[0,-1],[-1,0]]
N,M=map(int,input().split())
cheese = [0]*N
for i in range(N):
    cheese[i] = list(map(int,input().split()))

hour = 0
cnt=0
while cheese != [[0]*M]*N:
    hour+=1
    cnt = 0
    visit = [[0]*M for _ in range(N)]
    que = [[0,0]]
    visit[0][0] = 2
    while que != []:
        i,j=que.pop()
        for k in direction:
            ni=i+k[0]
            nj=j+k[1]
            if 0<=ni<N and 0<=nj<M:
                if cheese[ni][nj] == 0 and visit[ni][nj] == 0:
                    visit[ni][nj] = 2
                    que.append([ni,nj])
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                for k in direction:
                    ni=i+k[0]
                    nj=j+k[1]
                    if cheese[i][j]==1 and visit[ni][nj] == 2:
                        cheese[i][j] = 0
                        cnt+=1
                        break
                else:
                    cnt+=1
print(hour)
print(cnt)