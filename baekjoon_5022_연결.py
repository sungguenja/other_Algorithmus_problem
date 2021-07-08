from collections import deque
from sys import stdin
input = stdin.readline
N,M = map(int,input().split())
visit = [[-1]*(M+1) for _ in range(N+1)]
A1 = tuple(map(int,input().split()))
A2 = tuple(map(int,input().split()))
B1 = tuple(map(int,input().split()))
B2 = tuple(map(int,input().split()))

def drawARectalgle(A_1,A_2):
    if A_1[0] > A_2[0]:
        for i in range(A_2[0],A_1[0]+1,1):
            visit[i][A_2[1]] = 0
            visit[i][A_1[1]] = 0
    else:
        for i in range(A_2[0],A_1[0]-1,-1):
            visit[i][A_2[1]] = 0
            visit[i][A_1[1]] = 0
    
    if A_1[1] > A_2[1]:
        for j in range(A_2[1],A_1[1]+1,1):
            visit[A_1[0]][j] = 0
            visit[A_2[0]][j] = 0
    else:
        for j in range(A_2[1],A_1[1]-1,-1):
            visit[A_1[0]][j] = 0
            visit[A_2[0]][j] = 0
    
    return abs(A_1[0]-A_2[0]) + abs(A_1[1]-A_2[1])

answer = drawARectalgle(A1,A2)

def drawBRectagle(B_1,B_2,N,M,A_1,A_2):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    answer = makeAnswer(B_1,B_2,N,M)
    Queue = deque()
    if visit[B_1[0]][B_1[1]] != -1 or A_1[0] == A_2[0] or A_1[1] == A_2[1]:
        Queue.append((B_1[0],B_1[1],False,0))
    else:
        Queue.append((B_1[0],B_1[1],True,0))
    visit[B_1[0]][B_1[1]] = 0

    if answer != N*M:
        return answer
        
    while Queue:
        i,j,trigger,cnt = Queue.popleft()
        
        if cnt > answer:
            continue

        if i == B_2[0] and j == B_2[1]:
            if answer > cnt:
                answer = cnt
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<=N and 0<=nj<=M:
                if visit[ni][nj] == 0 and trigger:
                    Queue.append((ni,nj,False,cnt+1))
                elif visit[ni][nj] == -1 or visit[ni][nj] >= cnt + 1:
                    visit[ni][nj] = cnt + 1
                    Queue.append((ni,nj,trigger,cnt+1))
    
    return answer

def makeAnswer(B_1,B_2,N,M):
    if visit[B_1[0]][B_1[1]] and visit[B_2[0]][B_2[1]]:
        if B_1[0] == B_2[0]:
            if 0 < B_1[1]+1 < M and visit[B_1[0]][B_1[1]+1] == 0 and visit[B_1[0]][B_1[1]-1] == 0:
                return abs(B_1[0]-B_2[0]) + abs(B_1[1]-B_2[1])
        if B_1[1] == B_2[1]:
            if 0 < B_1[0]+1 < N and visit[B_1[0]+1][B_1[1]] == 0 and visit[B_1[0]-1][B_1[1]] == 0:
                return abs(B_1[0]-B_2[0]) + abs(B_1[1]-B_2[1])
    return N*M

B_answer = drawBRectagle(B1,B2,N,M,A1,A2)
if B_answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer + B_answer)