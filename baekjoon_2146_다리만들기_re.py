from collections import deque
from sys import stdin
input = stdin.readline

def findStartPoint(miles,N):
    startPoint = []
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for i in range(N):
        for j in range(N):
            if miles[i][j] == 1:
                continue
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N and miles[ni][nj] != 0:
                    startPoint.append((i,j,miles[ni][nj]))
                    break
    return startPoint

def makePartitionNumber(miles,N):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    partitionNumber = 0
    partitionMiles = [[0]*N for _ in range(N)]
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miles[i][j] == 1 and partitionMiles[i][j] == 0 and visit[i][j] == False:
                partitionNumber += 1
                Que = deque()
                Que.append((i,j))
                partitionMiles[i][j] = partitionNumber
                visit[i][j] = True
                while Que:
                    si,sj = Que.popleft()
                    for k in range(4):
                        ni = si + di[k]
                        nj = sj + dj[k]
                        if 0<=ni<N and 0<=nj<N and miles[ni][nj] == 1 and visit[ni][nj] == False:
                            visit[ni][nj] = True
                            partitionMiles[ni][nj] = partitionNumber
                            Que.append((ni,nj))
    return partitionMiles


def bfs(miles,i,j,startNumber,N,maximumDistance):
    visit = [[N**2]*N for _ in range(N)]
    answer = maximumDistance
    Que = deque()
    Que.append((i,j,1))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    while Que:
        si,sj,distance = Que.popleft()
        if miles[si][sj] != 0 and miles[si][sj] != startNumber:
            if answer > distance - 1:
                answer = distance - 1
            continue
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if  0<=ni<N and 0<=nj<N and miles[ni][nj] != startNumber and distance + 1 < visit[ni][nj]:
                visit[ni][nj] = distance + 1
                Que.append((ni,nj,distance+1))
    return answer

N = int(input())

miles = [list(map(int,input().split())) for i in range(N)]
partitionMiles = makePartitionNumber(miles,N)
startPointList = findStartPoint(partitionMiles,N)
answer = N**2

for startPoint in startPointList:
    startI, startJ, startNumber = startPoint
    nowDistance = bfs(partitionMiles,startI,startJ,startNumber,N,answer)
    if answer > nowDistance:
        answer = nowDistance

print(answer)