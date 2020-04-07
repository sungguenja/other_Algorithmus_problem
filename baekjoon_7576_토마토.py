M,N = map(int,input().split())

tomato = [0]*N
zero_stack = 0
que = [0]*N*M*2
l=0
r=0
visit = [[False]*M for _ in range(N)]
for i in range(N):
    horizon = []
    horizon = list(map(int,input().split()))
    for j in range(M):
        if horizon[j] == 0:
            zero_stack += 1
        elif horizon[j] == 1:
            que[r] = [i,j]
            visit[i][j] = 0
            r+=1
    tomato[i] = horizon[:]

day=0
direction = [[0,1],[1,0],[0,-1],[-1,0]]
while l != r:
    now = que[l]
    i,j=now[0],now[1]
    l+=1
    for k in direction:
        ni=i+k[0]
        nj=j+k[1]
        if 0<=ni<N and 0<=nj<M:
            if tomato[ni][nj] == 0 and (visit[ni][nj] == False or visit[ni][nj]>visit[i][j]+1):
                visit[ni][nj] = visit[i][j]+1
                que[r] = [ni,nj]
                r+=1
                if visit[ni][nj] > day:
                    day = visit[ni][nj]
                zero_stack -= 1
                if zero_stack == 0:
                    break
    if zero_stack == 0:
        break

if zero_stack != 0:
    day = -1
print(day)