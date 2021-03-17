from collections import deque
N = int(input())
answer = 0
area = [list(map(int,input().split())) for i in range(N)]
visit = [[False]*N for i in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(start_i,start_j,check_number):
    Que = deque()
    Que.append((start_i,start_j))
    visit[start_i][start_j] = True
    while Que:
        i,j = Que.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N:
                if visit[ni][nj] == False and area[ni][nj] == check_number:
                    visit[ni][nj] = True
                    Que.append((ni,nj))

for i in range(N):
    for j in range(N):
        if visit[i][j] == False:
            answer += 1
            bfs(i,j,area[i][j])

print(answer)