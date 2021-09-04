from sys import stdin
from collections import deque
input = stdin.readline

N,M,K = map(int,input().split())
maze = [list(input().strip()) for i in range(N)]

def bfs(N,M,K):
    answer = N*M*K*4
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    Que = deque()
    Que.append((0,0,1,0,0))
    visit = [[[False]*M for _ in range(N)] for i in range(K+1)]
    for k in range(K+1):
        visit[k][0][0] = True

    while Que:
        i,j,cnt,wall,day = Que.popleft()
        
        if i == N-1 and j == M-1:
            if cnt < answer:
                answer = cnt
            return answer

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<M:
                if maze[ni][nj] == '0':
                    if not visit[wall][ni][nj]:
                        visit[wall][ni][nj] = True
                        Que.append((ni,nj,cnt+1,wall,(day+1)%2))
                else:
                    if wall < K and not visit[wall+1][ni][nj]:
                        if day == 0:
                            visit[wall+1][ni][nj] = True
                            Que.append((ni,nj,cnt+1,wall+1,(day+1)%2))
                        else:
                            Que.append((i,j,cnt+1,wall,(day+1)%2))
    return answer

answer = bfs(N,M,K)
if answer == N*M*K*4:
    print(-1)
else:
    print(answer)