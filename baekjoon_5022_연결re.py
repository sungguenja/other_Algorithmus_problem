from collections import deque
N,M = map(int,input().split())
A1 = tuple(map(int,input().split()))
A2 = tuple(map(int,input().split()))
B1 = tuple(map(int,input().split()))
B2 = tuple(map(int,input().split()))

def drawARectalgle(A_1,A_2):
    first_route = [A_1]
    second_route = [A_1]
    if A_1[0] > A_2[0]:
        for i in range(A_2[0],A_1[0]+1,1):
            first_route.append((i,A_2[1]))
            second_route.append((i,A_1[1]))
    else:
        for i in range(A_2[0],A_1[0]-1,-1):
            first_route.append((i,A_2[1]))
            second_route.append((i,A_1[1]))
    
    if A_1[1] > A_2[1]:
        for j in range(A_2[1],A_1[1]+1,1):
            first_route.append((A_1[0],j))
            second_route.append((A_2[0],j))
    else:
        for j in range(A_2[1],A_1[1]-1,-1):
            first_route.append((A_1[0],j))
            second_route.append((A_2[0],j))
    
    return first_route, second_route, abs(A_1[0]-A_2[0]) + abs(A_1[1]-A_2[1])

first_route, second_route, answer = drawARectalgle(A1,A2)

def bfs(start,end,cant,N,M):
    print(cant)
    if start in cant:
        return (N*M+1)**2
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[False]*(M+1) for _ in range(N+1)]
    answer = (N*M+1)**2
    Que = deque()
    Que.append((start[0],start[1],0))
    while Que:
        i,j,cnt = Que.popleft()
        if cnt > 15:
            print(i,j)
        if cnt > answer:
            continue

        if i == end[0] and j == end[1]:
            if cnt < answer:
                answer = cnt
            continue
            
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<=N and 0<=nj<=M and not visit[ni][nj]:
                if (ni,nj) not in cant:
                    visit[ni][nj] = True
                    Que.append((ni,nj,cnt+1))

    return answer
before_answer = bfs(B1,B2,first_route,N,M)
B_answer = min(before_answer,bfs(B1,B2,second_route,N,M))

if B_answer == (N*M+1)**2:
    print("IMPOSSIBLE")
else:
    print(answer + B_answer)