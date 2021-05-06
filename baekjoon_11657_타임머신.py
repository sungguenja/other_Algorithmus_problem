import sys
INF = sys.maxsize
input = sys.stdin.readline

def bellmanFord(graph,start,length):
    dist = [INF]*(length)
    dist[start] = 0
    
    for _ in range(length-1):
        for start,end,weight in graph:
            if dist[start] != INF:
                dist[end] = min(dist[end],dist[start] + weight)
                
    return dist

def isCycle(dist,graph):
    for start,end,weight in graph:
        if dist[start] != INF and dist[end] > dist[start] + weight:
            return True
    return False

N,M = map(int,input().split())
graph = []
for _ in range(M):
    start,end,weight = map(int,input().split())
    graph.append((start-1,end-1,weight))
    
dist = bellmanFord(graph,0,N)
if isCycle(dist,graph):
    print(-1)
else:
    for i in dist[1:]:
        if i == INF:
            print(-1)
        else:
            print(i)