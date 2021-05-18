import sys
sys.setrecursionlimit(100000)
di = [-1,-1,-1,0,1,0]
dj = [-1,0,1,1,1,0]
result = 0
def makeNextMaze(now_maze):
    result_maze = [['.']*8 for i in range(8)]
    for i in range(1,8):
        for j in range(8):
            result_maze[i][j] = now_maze[i-1][j]
    return result_maze

def moveInMaze(now_maze,start_i=7,start_j=0):
    global result
    if result == 1:
        return
    if start_i == 0 and start_j == 7:
        result = 1
        return
    if now_maze[start_i][start_j] == '#':
        return
    for k in range(6):
        ni = start_i + di[k]
        nj = start_j + dj[k]
        if 0<=ni<8 and 0<=nj<8 and now_maze[ni][nj] == '.':
            moveInMaze(makeNextMaze(now_maze),ni,nj)

maze = [list(input()) for i in range(8)]
moveInMaze(maze)
print(result)