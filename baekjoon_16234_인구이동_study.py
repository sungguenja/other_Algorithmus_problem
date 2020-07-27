from copy import deepcopy
di = [0,1,0,-1]
dj = [1,0,-1,0]
N,L,R = map(int,input().split())
earth = [list(map(int,input().split())) for _ in range(N)]
before_earth = []
day = 0
while before_earth != earth:
    before_earth = deepcopy(earth)
    visit = [[False]*N for _ in range(N)]
    cnt = False
    que = [0]*(N**2)
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<N and 0<=nj<N and not visit[ni][nj]:
                        if L<=abs(earth[i][j]-earth[ni][nj])<=R:
                            que[x] = [i,j]
                            x+=1
                            visit[i][j] = True
                            answer = 0
                            while y<x:
                                ni,nj=que[y][0],que[y][1]
                                answer += earth[ni][nj]
                                y+=1
                                for k in range(4):
                                    nni = ni + di[k]
                                    nnj = nj + dj[k]
                                    if 0<=nni<N and 0<=nnj<N and not visit[nni][nnj]:
                                        if L<=abs(earth[nni][nnj]-earth[ni][nj])<=R:
                                            que[x] = [nni,nnj]
                                            x+=1
                                            visit[nni][nnj] = True
                            answer = answer//x
                            break
                if que != [0]*(N**2):
                    nx=0
                    while nx<N**2 and que[nx] != 0:
                        earth[que[nx][0]][que[nx][1]] = answer
                        nx+=1
                    if not cnt:
                        day += 1
                        cnt = True
                    que = [0]*(N**2)
                    x = 0
                    y = 0
print(day)