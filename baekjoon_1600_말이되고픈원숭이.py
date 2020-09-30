import sys
from collections import deque
dmi = [0,1,0,-1]
dmj = [1,0,-1,0]
dhi = [-2,-1,1,2,2,1,-1,-2]
dhj = [1,2,2,1,-1,-2,-2,-1]
K = int(input())
W,H=map(int,input().split())
travel = []
for i in range(H):
    travel.append(list(map(int,sys.stdin.readline().split())))
visit = [[[False for k in range(31)] for i in range(W)] for j in range(H)]
visit[0][0][K] = 1
answer = 10**5
Que = deque()
Que.append((0,0,K,0))
while Que:
    i,j,horse,cnt = Que.popleft()
    if i==H-1 and j==W-1:
        if cnt<answer:
            answer = cnt
        continue
    if horse>0:
        for k in range(8):
            ni = i+dhi[k]
            nj = j+dhj[k]
            if 0<=ni<H and 0<=nj<W and not visit[ni][nj][horse-1] and travel[ni][nj] != 1:
                visit[ni][nj][horse-1]=True
                Que.append((ni,nj,horse-1,cnt+1))
    for k in range(4):
        ni = i+dmi[k]
        nj = j+dmj[k]
        if 0<=ni<H and 0<=nj<W and not visit[ni][nj][horse] and travel[ni][nj] != 1:
            visit[ni][nj][horse]=True
            Que.append((ni,nj,horse,cnt+1))
if answer == 10**5:
    print(-1)
else:
    print(answer)