from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(minimum,maximum):
    Que = deque()
    Que.append((0,0))
    visit = [[0]*N for i in range(N)]
    while Que:
        i,j = Que.popleft()
        if i == N-1 and j == N-1:
            return True
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if visit[ni][nj] == 0 and minimum <= matrix[ni][nj] <= maximum:
                    visit[ni][nj] = 1
                    Que.append((ni,nj))
    return False

N = int(input())
matrix = [0]*N
minimum = 201
maximum = -1

for i in range(N):
    horizon = list(map(int,input().split()))
    minimum = min(minimum,min(horizon))
    maximum = max(maximum,max(horizon))
    matrix[i] = horizon[:]
answer = 500
minimum_to_maximum = min(matrix[0][0],matrix[N-1][N-1])
maximum_to_minimum = max(matrix[0][0],matrix[N-1][N-1])
left, right = minimum,maximum_to_minimum
while minimum <= left <= minimum_to_maximum and maximum_to_minimum <= right <= maximum:
    if bfs(left,right):
        answer = min(answer,right-left)
        left += 1
    else:
        right += 1

print(answer)