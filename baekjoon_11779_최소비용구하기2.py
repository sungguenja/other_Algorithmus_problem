import sys
from collections import deque
N = int(input())
bus_list = [[] for i in range(N+1)]
M = int(input())
for _ in range(M):
    start,goal,cost = map(int,input().split())
    bus_list[start].append((goal,cost))

start_point, end_point = map(int,input().split())
def dijkstra(bus,start,end):
    cost_list = [sys.maxsize]*len(bus)
    route_list = [False]*len(bus)
    Queue = deque()
    Queue.append((start,0,[str(start)]))
    while Queue:
        now,cost,route = Queue.popleft()
        for bus_goal_and_cost in bus[now]:
            goal,next_cost = bus_goal_and_cost[0],bus_goal_and_cost[1]+cost
            if next_cost < cost_list[goal]:
                cost_list[goal] = next_cost
                route_list[goal] = route + [str(goal)]
                Queue.append((goal,next_cost,route+[str(goal)]))
    return cost_list[end],route_list[end]

answer_cost, answer_bus_route = dijkstra(bus_list,start_point,end_point)
print(answer_cost)
print(len(answer_bus_route))
print(' '.join(answer_bus_route))