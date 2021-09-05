import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
cheese = []
day = 0
cheese_cnt = 0

def airBfs(i,j):
    Que = deque()
    Que.append((i,j))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    while Que:
        i,j = Que.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<M:
                if not visit[ni][nj]:
                    visit[ni][nj] = True
                    if cheese[ni][nj] == 1:
                        erase_chees[ni][nj] = True
                    else:
                        Que.append((ni,nj))

def checkCheese():
    for i in range(N):
        if not visit[i][0]:
            visit[i][0] = True
            airBfs(i,0)
        if not visit[i][M-1]:
            visit[i][M-1] = True
            airBfs(i,M-1)
    
    for j in range(M):
        if not visit[0][j]:
            visit[0][j] = True
            airBfs(0,j)
        if not visit[N-1][j]:
            visit[N-1][j] = True
            airBfs(N-1,j)

for i in range(N):
    horizon = list(map(int,input().split()))
    for j in range(M):
        if horizon[j] == 1:
            cheese_cnt += 1
    cheese.append(horizon)

while cheese_cnt > 0:
    visit = [[False]*M for i in range(N)]
    erase_chees = [[False]*M for i in range(N)]
    last_cheese = 0
    checkCheese()
    for i in range(N):
        for j in range(M):
            if erase_chees[i][j]:
                cheese[i][j] = 0
                erase_chees[i][j] = False
                cheese_cnt -= 1
                last_cheese += 1
    day += 1

print(day)
print(last_cheese)