import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
heap = []
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

first_goal,second_goal = map(int,input().split())

def dijkstra(start):
    distance = [INF]*(N+1)
    heapq.heappush(heap,(0,start))
    distance[start] = 0

    while heap:
        cost,now = heapq.heappop(heap)
        if distance[now] < cost:
            continue

        for goal, goal_cost in graph[now]:
            next_cost = goal_cost+cost
            if distance[goal] > next_cost:
                distance[goal] = next_cost
                heapq.heappush(heap,(next_cost,goal))
    
    return distance

start_distance = dijkstra(1)
first_distance = dijkstra(first_goal)
second_distance = dijkstra(second_goal)

answer_1 = sys.maxsize
answer_2 = sys.maxsize
flag_1 = False
flag_2 = False
if start_distance[first_goal] != INF and first_distance[second_goal] != INF and second_distance[N] != INF:
    answer_1 = start_distance[first_goal] + first_distance[second_goal] + second_distance[N]
else:
    flag_1 = True

if start_distance[second_goal] != INF and first_distance[N] != INF and second_distance[first_goal] != INF:
    answer_2 = start_distance[second_goal] + first_distance[N] + second_distance[first_goal]
else:
    flag_2 = True

if flag_1 and flag_2:
    print(-1)
else:
    print(min(answer_1,answer_2))