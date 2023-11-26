from sys import stdin
from collections import deque
input = stdin.readline

def bfs(cost,N):
    answer = 'sad'
    Que = deque()
    visit = [[False]*(N+2) for i in range(N+2)]
    Que.append(0)
    visit[0][0] = True
    while Que:
        if answer == 'happy':
            break
        
        start = Que.popleft()
        if start == N + 1:
            answer = 'happy'
            break
        
        for goal in range(N+2):
            if not visit[start][goal] and cost[start][goal] <= 20:
                Que.append(goal)
                visit[start][goal] = True
    
    return answer


T = int(input())

for _ in range(T):
    N = int(input())
    cost = [[0]*(N+2) for i in range(N+2)]
    position = [N]*(N+2)
    for i in range(N+2):
        position[i] = list(map(int,input().split()))
    for i in range(N+1):
        for j in range(i+1,N+2):
            nowCost = abs(position[i][0] - position[j][0]) + abs(position[i][1] - position[j][1])
            if (nowCost % 50 == 0):
                nowCost = nowCost // 50
                cost[i][j] = nowCost
                cost[j][i] = nowCost
            else:
                nowCost = nowCost // 50 + 1
                cost[i][j] = nowCost
                cost[j][i] = nowCost
            
    print(bfs(cost,N))