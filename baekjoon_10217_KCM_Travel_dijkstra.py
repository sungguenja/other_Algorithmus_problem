from collections import deque
import sys
INF = sys.maxsize
input = sys.stdin.readline
def dijkstra(route,max_cost,length):
    answer = INF
    Que = deque()
    Que.append((1,0,0))
    dijkstra_cost = [[INF]*(10001) for i in range(length+1)]
    dijkstra_cost[1][0] = 0
    while Que:
        now,cost,date = Que.popleft()
        if cost > max_cost or date >= answer:
            continue
        if now == length:
            if date < answer:
                answer = date
            continue
        for route_status in route[now]:
            goal,goal_cost,goal_date = route_status
            next_cost = cost + goal_cost
            next_date = date + goal_date
            if next_cost <= max_cost and (next_date < dijkstra_cost[goal][next_cost] and next_date < answer):
                dijkstra_cost[goal][next_cost] = next_date
                Que.append((goal,next_cost,next_date))
    return answer

for t in range(int(input())):
    N,max_cost,M = map(int,input().split())
    route = [[] for i in range(N+1)]
    for r in range(M):
        start, end, cost, day = map(int,input().split())
        route[start].append((end,cost,day))
    answer = dijkstra(route,max_cost,N)
    if answer == INF:
        answer = 'Poor KCM'
    print(answer)