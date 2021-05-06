from collections import deque
import sys
def dijkstra(graph,start,length,end):
    INF = sys.maxsize
    dist = [INF]*(length+1)
    Que = deque()
    Que.append((start,0))
    dist[start] = 0
    while Que:
        now,cost = Que.popleft()

        for goal, additional in graph[now]:
            next_cost = cost + additional
            if dist[goal] > next_cost:
                dist[goal] = next_cost
                Que.append((goal,next_cost))
    return dist[end]

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for i in range(n+1)]
    for start,goal,weight in fares:
        graph[start].append((goal,weight))
        graph[goal].append((start,weight))
    answer = dijkstra(graph,s,n,a) + dijkstra(graph,s,n,b)
    for i in range(1,n+1):
        answer = min(answer,dijkstra(graph,s,n,i)+dijkstra(graph,i,n,a)+dijkstra(graph,i,n,b))
    return answer