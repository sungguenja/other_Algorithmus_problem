from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

route = [list(map(int,input().split())) for _ in range(N)]

tour_list = list(map(int,input().split()))
def bfs(start,goal):
    Que = deque()
    Que.append(start)
    visit = [False]*N
    visit[start-1] = True
    while Que:
        now = Que.popleft()
        if now == goal:
            return False
        
        for end in range(1,N+1):
            if route[now-1][end-1] == 1 and not visit[end-1]:
                visit[end-1] = True
                Que.append((end))
    return True

for start in range(M-1):
    if bfs(tour_list[start],tour_list[start+1]):
        print("NO")
        break
else:
    print("YES")