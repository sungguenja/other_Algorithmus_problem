from collections import deque
def bfs(start,goal,N,K):
    visit = [False]*(N+1)
    Que = deque()
    Que.append((start,0))
    answer = N*K
    while Que:
        now,cnt = Que.popleft()

        if cnt >= answer:
            continue

        if now == goal:
            if answer > cnt:
                answer = cnt
            continue

        if 0 < (now + K - 2) // K and (now + K - 2) // K == (goal + K - 2) // K:
            if answer > cnt + 2:
                answer = cnt + 2
            continue

        if not visit[(now + K - 2) // K] and 0 < (now + K - 2) // K:
            Que.append(((now + K - 2) // K,cnt+1))
        
        for i in range(now*K-(K-2),now*K+2):
            if 0 < i <= N and not visit[i]:
                Que.append((i,cnt+1))
            elif i <= 0 or i > N:
                break
    
    return answer
    
N,K,Q = map(int,input().split())
for i in range(Q):
    start,goal = map(int,input().split())
    print(bfs(start,goal,N,K))