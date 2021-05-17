import sys
INF = sys.maxsize
input = sys.stdin.readline

def dp(route,max_cost,end):
    cost_route = [[INF]*(max_cost+1) for i in range(end+1)]
    cost_route[1][0] = 0
    for cost in range(max_cost+1):
        for airport in range(1,end+1):
            if cost_route[airport][cost] == INF:
                continue
            now_date = cost_route[airport][cost]
            for status in route[airport]:
                goal,goal_cost,goal_date = status
                next_cost = cost+goal_cost
                next_date = now_date+goal_date
                if next_cost > max_cost:
                    continue
                if next_date < cost_route[goal][next_cost]:
                    cost_route[goal][next_cost] = next_date
    answer = min(cost_route[end])
    return answer

for t in range(int(input())):
    N,max_cost,M = map(int,input().split())
    route = [[] for i in range(N+1)]
    for i in range(M):
        start,goal,cost,date = map(int,input().split())
        route[start].append((goal,cost,date))
    answer = dp(route,max_cost,N)
    if answer == INF:
        answer = 'Poor KCM'
    print(answer)