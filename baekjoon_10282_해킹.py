from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(dependencies,start_computer):
    N = len(dependencies)
    visit = [INF]*N
    visit[start_computer] = 0
    Que = deque()
    Que.append((start_computer,0))
    while Que:
        now_computer,date = Que.popleft()
        for i in range(len(dependencies[now_computer])):
            goal_computer, cost = dependencies[now_computer][i]
            next_cost = cost + date
            if next_cost < visit[goal_computer]:
                visit[goal_computer] = next_cost
                Que.append((goal_computer,next_cost))
    
    answer_date = -1
    answer_computer = 0
    for i in range(1,N):
        if visit[i] != INF:
            answer_computer += 1
            if answer_date < visit[i]:
                answer_date = visit[i]
            
    return str(answer_computer), str(answer_date)
        

for t in range(int(input())):
    n,d,c = map(int,input().split())
    dependencies = [[] for i in range(n+1)]
    for i in range(d):
        start_computer, end_computer, day = map(int,input().split())
        dependencies[end_computer].append((start_computer,day))
        
    print(" ".join(dijkstra(dependencies,c)))