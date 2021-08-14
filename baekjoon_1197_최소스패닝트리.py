import sys
INF = sys.maxsize
input = sys.stdin.readline

N,M = map(int,input().split())
weight = [[] for i in range(N)]
for i in range(M):
    start,end,cost = map(int,input().split())
    weight[start-1].append((end-1,cost))
    weight[end-1].append((start-1,cost))

def getMinVertex(dist,selected):
    minimum_value = INF
    minv = 0
    for i in range(len(dist)):
        if not selected[i] and minimum_value > dist[i]:
            minimum_value = dist[i]
            minv = i
    return minv

def MSTPrim(N,weight):
    dist = [INF]*N
    dist[0] = 0
    selected = [False]*N

    for i in range(N):
        u = getMinVertex(dist,selected)
        selected[u] = True

        for v in range(len(weight[u])):
            if not selected[weight[u][v][0]] and weight[u][v][1] < dist[weight[u][v][0]]:
                dist[weight[u][v][0]] = weight[u][v][1]
                
    return dist

print(sum(MSTPrim(N,weight)))