N,K = map(int,input().split())
answer = N*K*100000
visit = [0]*100001
Que = [[N,0]]
answer = (N+1)*(K+1)*100000
move = [-1,1]
while Que != []:
    now,cnt = Que.pop(0)
    if cnt>=answer:
        continue
    if now == K:
        if answer>cnt:
            answer = cnt
        continue
    for k in range(3):
        if k == 0:
            nx = now*2
        else:
            nx = now + move[k-1]

        if 0<=nx<=100000 and (visit[nx] == 0 or nx==K):
            visit[nx] = 1
            Que.append([nx,cnt+1])
print(answer)