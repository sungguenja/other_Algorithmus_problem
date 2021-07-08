from collections import deque
N,M = map(int,input().split())
A1 = tuple(map(int,input().split()))
A2 = tuple(map(int,input().split()))
B1 = tuple(map(int,input().split()))
B2 = tuple(map(int,input().split()))

def firstBfs(start,end,next_start,next_goal,N,M):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    Que = deque()
    answer = (N*M+1)**2
    after_answer = (N*M+1)**2
    visit = [[False]*(M+1) for _ in range(N+1)]
    Que.append((start[0],start[1],0,[(start[0],start[1])]))
    while Que:
        i,j,cnt,route = Que.popleft()

        if i == end[0] and j == end[1]:
            answer = cnt
            print(answer)
            after_answer = min(after_answer,secondBfs(next_start,next_goal,N,M,route))
        
        if after_answer != (N*M+1)**2 and answer != (N*M+1)**2:
            return after_answer + answer

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<=N and 0<=nj<=M and not visit[ni][nj] and (ni,nj) != next_start and (ni,nj) != next_goal:
                visit[ni][nj] = True
                Que.append((ni,nj,cnt+1,route+[(ni,nj)]))
    
    return "IMPOSSIBLE"

def secondBfs(start,end,N,M,cant):
    print(cant)
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    Que = deque()
    answer = (N*M+1)**2
    Que.append((start[0],start[1],0))
    visit = [[False]*(M+1) for _ in range(N+1)]
    Que.append((start[0],start[1],0))
    while Que:
        i,j,cnt = Que.popleft()

        if cnt >= answer:
            continue

        if i == end[0] and j == end[1]:
            if cnt < answer:
                answer = cnt
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<=N and 0<=nj<=M and not visit[ni][nj] and (ni,nj) not in cant:
                visit[ni][nj] = True
                Que.append((ni,nj,cnt+1))
    print(answer)
    return answer

print(firstBfs(A1,A2,B1,B2,N,M))