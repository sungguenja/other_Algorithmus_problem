from sys import stdin
from collections import deque
input = stdin.readline

N,M,K = map(int,input().split())
maze = [list(input()) for i in range(N)]

def bfs(N,M,K):
    answer = N*M*K*4
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    Que = deque()
    Que.append((0,0,1,0,0))
    visit = [[[[-1]*M for i in range(N)] for j in range(K+1)] for _ in range(2)]

    while Que:
        i,j,cnt,block,day = Que.popleft()
        
        if cnt >= answer:
            continue

        if i == N-1 and j == M-1:
            if cnt < answer:
                answer = cnt
            continue

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<M:
                if maze[ni][nj] == '0':
                    if visit[(day+1)%2][block][ni][nj] == -1 or visit[(day+1)%2][block][ni][nj] > cnt + 1:
                        visit[(day+1)%2][block][ni][nj] = cnt + 1
                        Que.append((ni,nj,cnt+1,block,(day+1)%2))
                else:
                    if block < K:
                        if day == 0:
                            if visit[(day+1)%2][block+1][ni][nj] == -1 or visit[(day+1)%2][block+1][ni][nj] > cnt + 1:
                                visit[(day+1)%2][block+1][ni][nj] = cnt + 1
                                Que.append((ni,nj,cnt+1,block+1,(day+1)%2))
                        else:
                            if visit[(day+2)%2][block+1][ni][nj] == -1 or visit[(day+2)%2][block+1][ni][nj] > cnt + 2:
                                visit[(day+2)%2][block+1][ni][nj] = cnt + 2
                                Que.append((ni,nj,cnt+2,block+1,(day+2)%2))
    return answer

answer = bfs(N,M,K)
if answer == N*M*K*4:
    print(-1)
else:
    print(answer)