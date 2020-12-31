from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]
N=int(input())
miles = [list(map(int,input().split())) for i in range(N)]
check_isl = [[0]*N for i in range(N)]
cnt = 1
answer = (N+1)**2
for i in range(N):
    for j in range(N):
        if miles[i][j] == 1 and check_isl[i][j] == 0:
            check_isl[i][j] = cnt
            Que = deque()
            Que.append([i,j])
            while len(Que) > 0:
                y,x = Que.popleft()
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0<=ni<N and 0<=nj<N and miles[ni][nj] == 1 and check_isl[ni][nj] == 0:
                        check_isl[ni][nj] = cnt
                        Que.append([ni,nj])
            cnt+=1
global_visit = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if check_isl[i][j] != 0 and global_visit[i][j] == 0:
            global_visit[i][j] = 1
            Que = deque()
            Que.append([i,j,0,check_isl[i][j]])
            visit = [[-1]*N for k in range(N)]
            while len(Que) > 0:
                y,x,d,isl = Que.popleft()
                if d>answer:
                    continue
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0<=ni<N and 0<=nj<N and (visit[ni][nj] == -1 or visit[ni][nj]>d+1):
                        if check_isl[ni][nj] == 0:
                            visit[ni][nj] = d+1
                            Que.append([ni,nj,d+1,isl])
                        elif check_isl[i][j] == check_isl[ni][nj]:
                            visit[ni][nj] = 0
                            global_visit[ni][nj] = 1
                            Que.append([ni,nj,0,isl])
                        elif check_isl[ni][nj] != 0 and check_isl[i][j] != check_isl[ni][nj]:
                            if d<answer:
                                answer = d

print(answer)