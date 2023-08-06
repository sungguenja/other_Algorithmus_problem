from collections import deque
from sys import stdin
input = stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]

M,N = map(int,input().split())
miro = [list(input()) for _ in range(N)]
visit = [[-1]*M for _ in range(N)]

que = deque()
que.append([0,0])
visit[0][0] = 0

while que:
    i,j = que.popleft()

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M:
            if miro[ni][nj] == '0' and (visit[ni][nj] == -1 or visit[ni][nj] > visit[i][j]):
                visit[ni][nj] = visit[i][j]
                que.append([ni,nj])
            elif miro[ni][nj] == '1' and (visit[ni][nj] == -1 or visit[ni][nj] > visit[i][j] + 1):
                visit[ni][nj] = visit[i][j] + 1
                que.append([ni,nj])
            

print(visit[-1][-1])