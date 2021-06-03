from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
room = [input() for i in range(N)]

def roomChecker(start_i,start_j,size_i,size_j,number):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    cnt = 1
    visit[start_i][start_j] = True
    Que = deque()
    Que.append((start_i,start_j))
    tmp[start_i][start_j] = number
    while Que:
        i,j = Que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<size_i and 0<=nj<size_j and not visit[ni][nj] and room[ni][nj] == '0':
                cnt += 1
                tmp[ni][nj] = number
                visit[ni][nj] = True
                Que.append((ni,nj))
    return cnt


tmp = [[0]*M for i in range(N)]
visit = [[False]*M for i in range(N)]
room_cnt = {}
number = 1
for i in range(N):
    for j in range(M):
        if room[i][j] == '0' and tmp[i][j] == 0:
            room_cnt[number] = roomChecker(i,j,N,M,number)
            number += 1

def bfs(start_i,start_j,size_i,size_j):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    result = 1
    visit = set()
    for k in range(4):
        ni = start_i + di[k]
        nj = start_j + dj[k]
        if 0<=ni<size_i and 0<=nj<size_j and tmp[ni][nj] != 0 and tmp[ni][nj] not in visit:
            visit.add(tmp[ni][nj])
            result += room_cnt[tmp[ni][nj]]
    return str(result%10)

answer = [['0']*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if tmp[i][j] == 0:
            answer[i][j] = bfs(i,j,N,M)

for ans in answer:
    print(''.join(ans))