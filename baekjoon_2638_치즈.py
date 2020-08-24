direction = [[0,1],[1,0],[0,-1],[-1,0]]
N,M=map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
last = [[0]*M for _ in range(N)]
while cheese != last:
    visit = [[0]*M for _ in range(N)]
    Que = []
    for i in range(N):
        if cheese[i][0] == 0:
            Que.append([i,0])
            visit[i][0] = -1
        if cheese[i][M-1] == 0:
            Que.append([i,M-1])
            visit[i][M-1] = -1
    for j in range(M):
        if cheese[0][j] == 0:
            Que.append([0,j])
            visit[0][j] = -1
        if cheese[N-1][j] == 0:
            Que.append([N-1,j])
            visit[N-1][j] = -1
    while Que != []:
        i,j = Que.pop(0)
        for k in direction:
            ni = i + k[0]
            nj = j + k[1]
            if 0<=ni<N and 0<=nj<M:
                if cheese[ni][nj] == 0 and visit[ni][nj] == 0:
                    Que.append([ni,nj])
                    visit[ni][nj] = -1
                elif cheese[ni][nj] == 1:
                    visit[ni][nj] += 1
    for i in range(N):
        for j in range(M):
            if visit[i][j] >= 2:
                cheese[i][j]=0
    cnt += 1
print(cnt)