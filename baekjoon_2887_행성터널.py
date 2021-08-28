import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = [False]*N
for i in range(N):
    arr[i] = tuple(map(int,input().split()))

weight = [[None]*N for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        distance = min(abs(arr[i][0]-arr[j][0]),abs(arr[i][1]-arr[j][1]),abs(arr[i][2]-arr[j][2]))
        weight[i][j] = distance
        weight[j][i] = distance

def getMinVertex(dist,selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and mindist > dist[v]:
            mindist = dist[v]
            minv = v
            
    return minv

def MSTPrim(N,weight):
    dist = [INF]*N
    selected = [False]*N
    dist[0] = 0

    for i in range(N):
        u = getMinVertex(dist,selected)
        selected[u] = True

        for v in range(N):
            if weight[i][v] != None:
                if not selected[v] and weight[u][v] < dist[v]:
                    dist[v] = weight[u][v]
    
    return dist

print(sum(MSTPrim(N,weight)))