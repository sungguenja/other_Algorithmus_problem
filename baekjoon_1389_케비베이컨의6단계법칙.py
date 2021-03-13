from collections import deque
N,E = map(int,input().split())
friend = [[] for i in range(N+1)]
for i in range(E):
    fre1,fre2 = map(int,input().split())
    friend[fre1].append(fre2)
    friend[fre2].append(fre1)

kevin_score = ((N+1)*(E+1))**2
kevin_answer = 0
def bfs(start,end,people):
    visit = [False]*(people+1)
    Que = deque()
    Que.append((start,0))
    answer = 0
    while Que:
        now,score = Que.popleft()
        if now == end:
            if answer == 0 or answer > score:
                answer = score
            continue
        for fre in friend[now]:
            if not visit[fre]:
                visit[fre] = True
                Que.append((fre,score+1))
    return answer

for start in range(1,N+1):
    sum_score = 0
    for goal in range(1,N+1):
        if start==goal:
            continue
        sum_score += bfs(start,goal,N)
    if kevin_score > sum_score:
        kevin_score = sum_score
        kevin_answer = start

print(kevin_answer)