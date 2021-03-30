from copy import deepcopy
from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]

def moveCluster(cluster,original):
    for origin in original:
        cave[origin[0]][origin[1]] = '.'

    for clust in cluster:
        cave[clust[0]][clust[1]] = 'x'

def goDown(point):
    return point[0]+1,point[1]

def gravity(cluster,original):
    trigger = True
    for clust in cluster:
        c_i, c_j = clust[0],clust[1]
        if c_i + 1 >= R or (cave[c_i+1][c_j] == 'x' and (c_i+1,c_j) not in cluster and [c_i+1,c_j] not in original):
            trigger = False
            break

    if trigger:
        gravity(deepcopy(deque(map(goDown,cluster))),deepcopy(original))
    else:
        moveCluster(deepcopy(cluster),deepcopy(original))
        

def checkCluster(highest,start):
    for case in range(4):
        trigger = True
        cluster = deque()
        if 0<=highest+di[case]<R and 0<=start+dj[case]<C and cave[highest+di[case]][start+dj[case]] == 'x':
            Que = deque()
            visit = [[False]*C for k in range(R)]
            Que.append((highest+di[case],start+dj[case]))
            cluster = deque()
            cluster.append([highest+di[case],start+dj[case]])
            while Que:
                i,j = Que.popleft()
                if i==R-1:
                    trigger = False
                    break
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<R and 0<=nj<C:
                        if visit[ni][nj] == False and cave[ni][nj] == 'x':
                            Que.append((ni,nj))
                            cluster.append([ni,nj])
                            visit[ni][nj] = True
        if trigger and len(cluster) != 0:
            gravity(deepcopy(deque(map(goDown,cluster))),deepcopy(cluster))
            break

def mining(timing,highest):
    switch = 1
    start = 0
    if timing%2 == 1:
        switch = -1
        start = C - 1
    
    while cave[highest][start] != 'x':
        start += switch
        if start < 0 or start >= C:
            return
    
    cave[highest][start] = '.'
    checkCluster(highest,start)

R,C = map(int,input().split())
cave = [list(input()) for i in range(R)]
N = int(input())
throw = list(map(int,input().split()))
for t in range(N):
    mining(t,R-throw[t])

for k in cave:
    print(''.join(k))