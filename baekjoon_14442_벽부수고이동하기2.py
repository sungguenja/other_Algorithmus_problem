from collections import deque

N,M,K = map(int,input().split())
maze = [list(input()) for i in range(N)]
visit = [[[False]*M for i in range(N)] for j in range(K+1)]
Que = deque()
answer = N*M*(K+1)
Que.append((0,0,0,1))

di = [0,1,0,-1]
dj = [1,0,-1,0]

while Que:
    now_i,now_j,now_k,cnt = Que.popleft()
    if cnt > answer:
        continue
    if now_i == N-1 and now_j == M-1:
        if cnt < answer:
            answer = cnt
        continue

    for k in range(4):
        ni = now_i + di[k]
        nj = now_j + dj[k]
        if 0<=ni<N and 0<=nj<M:
            if maze[ni][nj] == '0' and not visit[now_k][ni][nj]:
                visit[now_k][ni][nj] = True
                Que.append((ni,nj,now_k,cnt+1))
            elif maze[ni][nj] == '1' and now_k + 1 <= K and not visit[now_k+1][ni][nj]:
                visit[now_k+1][ni][nj] = True
                Que.append((ni,nj,now_k+1,cnt+1))

if answer == N*M*(K+1):
    answer = -1

print(answer)