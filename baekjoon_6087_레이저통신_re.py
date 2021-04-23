from collections import deque
import sys
input = sys.stdin.readline
def solution(start,end,room,N,M):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    result = (N+1)*(M+1)*2
    visit = [[[-1]*4 for j in range(N)] for i in range(M)]
    Que = deque()
    Que.append((start[0],start[1],0,5))
    while Que:
        i,j,cost,direction = Que.popleft()
        if cost >= result:
            continue
        if i == end[0] and j == end[1]:
            if cost < result:
                result = cost
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<M and 0<=nj<N and (room[ni][nj] == '.' or room[ni][nj] == 'C'):
                if direction == 5:
                    visit[ni][nj][k] == cost
                    Que.append((ni,nj,cost,k))
                else:
                    if direction == k:
                        if visit[ni][nj][k] == -1 or visit[ni][nj][k] > cost:
                            visit[ni][nj][k] = cost
                            Que.append((ni,nj,cost,k))
                    elif direction == (k+2)%4:
                        continue
                    else:
                        if visit[ni][nj][k] == -1 or visit[ni][nj][k] > cost + 1:
                            visit[ni][nj][k] = cost+1
                            Que.append((ni,nj,cost+1,k))
    return result


N,M = map(int,input().split())
room = [0]*M
start = []
end = []
trigger = 0
for i in range(M):
    horizon = list(input())
    if trigger < 2:
        for j in range(N):
            if horizon[j] == 'C':
                if trigger == 0:
                    start = (i,j)
                else:
                    end = (i,j)
                trigger += 1
    room[i] = horizon[:]

answer = solution(start,end,room,N,M)
print(answer)