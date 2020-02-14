N,M=map(int,input().split())

maze = []
for _ in range(N):
    horizon = []
    horizon = list(input())
    maze.append(horizon)

maze[0][0] = 1
que = [[0,0]]
direction = [[0,1],[1,0],[0,-1],[-1,0]]
while que != []:
    X=que.pop(0)
    ni,nj=X[0],X[1]
    if ni==N-1 and nj==M-1:
        break
    for k in direction:
        if N>ni+k[0]>=0 and M>nj+k[1]>=0:
            if maze[ni+k[0]][nj+k[1]] == '1':
                maze[ni+k[0]][nj+k[1]] = maze[ni][nj] + 1
                que.append([ni+k[0],nj+k[1]])

print(maze[N-1][M-1])