import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
lines = [[] for _ in range(N+1)]

for i in range(M):
    a,b,cost = map(int,input().split())
    lines[a].append((b,cost))
    lines[b].append((a,cost))

def getStartPoint(dist,visit):
    minV = 0
    min_dist = INF
    for v in range(N+1):
        if not visit[v] and min_dist > dist[v]:
            min_dist = dist[v]
            minV = v
    return minV

def Prim():
    dist = [INF]*(N+1)
    visit = [False]*(N+1)
    dist[1] = 0

    for i in range(N):
        start = getStartPoint(dist,visit)
        visit[start] = True
        for (goal,cost) in lines[start]:
            if not visit[goal] and cost < dist[goal]:
                dist[goal] = cost
    
    return sum(dist[1:])

print(Prim())