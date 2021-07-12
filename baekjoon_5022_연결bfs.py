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
    visit[start[0]][start[1]] = True
    Que.append((start[0],start[1],0,[(start[0],start[1])]))
    while Que:
        i,j,cnt,route = Que.popleft()

        if i == end[0] and j == end[1]:
            tmp_answer = cnt
            tmp_after_answer = secondBfs(next_start,next_goal,N,M,route)
            if tmp_answer + tmp_after_answer < answer + after_answer:
                after_answer = tmp_after_answer
                answer = tmp_answer
        
        if cnt > after_answer + answer:
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<=N and 0<=nj<=M and not visit[ni][nj] and not ((ni == next_start[0] and nj == next_start[1]) or (ni == next_goal[0] and nj == next_goal[1])):
                visit[ni][nj] = True
                Que.append((ni,nj,cnt+1,route+[(ni,nj)]))
    
    if after_answer != (N*M+1)**2 and answer != (N*M+1)**2:
        return after_answer + answer

    return "IMPOSSIBLE"

def secondBfs(start,end,N,M,cant):
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
    return answer

tmp_answer_1 = firstBfs(A1,A2,B1,B2,N,M)
tmp_answer_2 = firstBfs(B1,B2,A1,A2,N,M)
if tmp_answer_1 != "IMPOSSIBLE" and tmp_answer_2 != "IMPOSSIBLE":
    print(min(tmp_answer_1,tmp_answer_2))
else:
    if tmp_answer_1 == "IMPOSSIBLE":
        print(tmp_answer_2)
    else:
        print(tmp_answer_1)