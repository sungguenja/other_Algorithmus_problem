from collections import deque
N,K = map(int,input().split())
Queue = deque()
visit = [-1]*(2*(K+N+1))
answer = 2*(K+N+1)
answer_route = []

if N < K:
    Queue.append((N,0,[str(N)]))
else:
    tmp = [str(N)]
    cnt = 0
    for i in range(N-1,K-1,-1):
        cnt += 1
        visit[i] = cnt
        tmp.append(str(i))
    Queue.append((K,cnt,tmp))

while Queue:
    now,cnt,route =  Queue.popleft()
    if cnt >= answer:
        continue

    if now == K:
        if cnt < answer:
            answer = cnt
            answer_route = route
        continue

    if 2*now < 2*(K+N+1) and (visit[2*now] == -1 or visit[2*now] > cnt + 1):
        visit[2*now] = cnt + 1
        Queue.append((2*now,cnt+1,route+[str(2*now)]))
    
    if now+1 < 2*(K+N+1) and (visit[now+1] == -1 or visit[now+1] > cnt + 1):
        visit[now+1] = cnt + 1
        Queue.append((now+1,cnt+1,route+[str(now+1)]))
    
    if now - 1 >= 0 and (visit[now-1] == -1 or visit[now-1] > cnt + 1):
        visit[now-1] = cnt + 1
        Queue.append((now-1,cnt+1,route+[str(now-1)]))

print(answer)
print(' '.join(answer_route))