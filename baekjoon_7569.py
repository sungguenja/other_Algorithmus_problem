direction = [[0,1,0],[1,0,0],[0,-1,0],[-1,0,0],[0,0,1],[0,0,-1]]
def bfs(N,M,H,start,zero):
    que = [0]*N*M*H*2
    front = -1
    rear = -1
    visit = [[[False]*M for _ in range(N)] for _ in range(H)]
    for s in start:
        rear += 1
        que[rear] = s
        visit[s[2]][s[0]][s[1]] = 0
    day=0
    while front != rear:
        front += 1
        i,j,k = que[front][0],que[front][1],que[front][2]
        for d in direction:
            ni=i+d[0]
            nj=j+d[1]
            nk=k+d[2]
            if 0<=ni<N and 0<=nj<M and 0<=nk<H:
                if tomato[nk][ni][nj] == 0 and (visit[nk][ni][nj] == False or visit[nk][ni][nj]>visit[k][i][j]+1):
                    visit[nk][ni][nj]=visit[k][i][j]+1
                    zero-=1
                    rear+=1
                    que[rear] = [ni,nj,nk]
                    if visit[nk][ni][nj]>day:
                        day = visit[nk][ni][nj]
            if zero == 0:
                break
        if zero == 0:
            break
    if zero != 0:
        day = -1
    return day

M,N,H=map(int,input().split())
tomato = [[0]*N for _ in range(H)]
start = []
zero = 0
for k in range(H):
    for i in range(N):
        horizon = []
        horizon = list(map(int,input().split()))
        for j in range(M):
            if horizon[j] == 0:
                zero += 1
            elif horizon[j] == 1:
                start.append([i,j,k])
        tomato[k][i] = horizon[:]
ans = bfs(N,M,H,start,zero)
print(ans)