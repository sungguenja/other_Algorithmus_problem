import heapq
import sys
INF = sys.maxsize

input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
graph = [[] for i in range(V)]
for i in range(E):
    u,v,w = map(int,input().split())
    graph[u-1].append([v-1,w])

dp = [INF]*V
Que = []

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(Que,(0,start))

    while Que:
        cost,now = heapq.heappop(Que)

        if dp[now] < cost:
            continue

        for goal, plus_cost in graph[now]:
            next_cost = plus_cost + cost

            if next_cost < dp[goal]:
                dp[goal] = next_cost
                heapq.heappush(Que,(next_cost,goal))

dijkstra(K-1)
for i in range(V):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])