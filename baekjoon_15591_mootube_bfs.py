from collections import deque
import sys
INF = sys.maxsize

def findUsadoUpperK(K,start,usado,N):
    cnt = 0
    Que = deque()
    visit = [False]*N
    visit[start] = True
    Que.append((start,INF))
    while Que:
        now,cost = Que.popleft()
        for goal,next_cost in usado[now]:
            next_cost = min(next_cost,cost)
            if next_cost != INF and next_cost>=K and not visit[goal]:
                visit[goal] = True
                cnt += 1
                Que.append((goal,next_cost))

    return cnt

input = sys.stdin.readline
N,M = map(int,input().split())
usado = [[] for i in range(N)]
for _ in range(N-1):
    start,goal,cost = map(int,input().split())
    usado[start-1].append((goal-1,cost))
    usado[goal-1].append((start-1,cost))


for _ in range(M):
    K,start = map(int,input().split())
    print(findUsadoUpperK(K,start-1,usado,N))