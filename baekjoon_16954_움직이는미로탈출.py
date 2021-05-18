from copy import deepcopy
from collections import deque
di = [0,-1,-1,-1,0,1,1,1,0]
dj = [0,-1,0,1,1,1,0,-1,-1]
result = 0
def makeNextMaze(now_maze):
    result_maze = [['.']*8 for i in range(8)]
    for i in range(1,8):
        for j in range(8):
            result_maze[i][j] = now_maze[i-1][j]
    return result_maze

def moveInMaze(now_maze,start_i=7,start_j=0):
    global result
    visit = [[[False]*8 for i in range(8)] for j in range(8)]
    Que = deque()
    Que.append((start_i,start_j,0))
    while Que:
        i,j,cost = Que.popleft()
        if i == 0 and j == 7:
            result = 1
            break
        if now_maze[cost][i][j] == '#':
            continue
        for k in range(9):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<8 and 0<=nj<8:
                if cost < 7:
                    if not visit[cost][ni][nj] and now_maze[cost][ni][nj] == '.' and now_maze[cost+1][ni][nj] == '.':
                        visit[cost][ni][nj] = True
                        Que.append((ni,nj,cost+1))
                else:
                    if not visit[cost][ni][nj] and now_maze[cost][ni][nj] == '.':
                        visit[cost][ni][nj] = True
                        Que.append((ni,nj,cost))

maze = [list(input()) for i in range(8)]
maze_list = [maze]
next_maze = deepcopy(maze)
for i in range(7):
    next_maze = makeNextMaze(next_maze)
    maze_list.append(next_maze)
maze_list = tuple(maze_list)
moveInMaze(maze_list)
print(result)