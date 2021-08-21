import sys
input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())
star_list = [tuple(map(int,input().split())) for i in range(N)]
linked_list = [tuple(map(int,input().split())) for i in range(M)]

weight = [[None]*N for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        dist = ((star_list[i][0] - star_list[j][0])**2 + (star_list[i][1] - star_list[j][1])**2)**0.5
        weight[i][j] = dist
        weight[j][i] = dist

for node in linked_list:
    weight[node[0]-1][node[1]-1] = 0
    weight[node[1]-1][node[0]-1] = 0

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

print("%.2f" %sum(MSTPrim(N,weight)))