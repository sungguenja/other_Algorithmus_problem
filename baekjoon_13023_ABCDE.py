from collections import deque
from sys import stdin
input = stdin.readline

globalAnswer = 0

def dfs(start,friendShip,visit,N,depth=1):
    global globalAnswer
    if globalAnswer == 1:
        return
    
    if depth == 4:
        globalAnswer = 1
        return
    
    for j in friendShip[start]:
        if globalAnswer == 1:
            return
        if visit[j] == False:
            visit[j] = True
            dfs(j,friendShip,visit,N,depth+1)
            visit[j] = False

N,M = map(int,input().split())
friendShip = [[] for _ in range(N)]

for _ in range(M):
    A,B = map(int,input().split())
    friendShip[A].append(B)
    friendShip[B].append(A)

for i in range(M):
    if globalAnswer == 1:
        break

    for j in friendShip[i]:
        if globalAnswer == 1:
            break

        visit = [False]*N
        visit[i] = True
        visit[j] = True
        dfs(j,friendShip,visit,N)
    
print(globalAnswer)