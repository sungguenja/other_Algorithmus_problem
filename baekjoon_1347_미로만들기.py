N = int(input())
command = input()
maze = [['#']]
di = [1,0,-1,0]
dj = [0,-1,0,1]
direction = 0
i = 0
j = 0
maze[i][j] = '.'
for k in range(N):
    now_command = command[k]
    if now_command == 'L':
        direction = (direction-1)%4
    elif now_command == 'R':
        direction = (direction+1)%4
    elif now_command == 'F':
        i = i + di[direction]
        j = j + dj[direction]
        if i == -1:
            maze = [['#']*len(maze[i])] + maze
            i = 0
            maze[i][j] = '.'
        elif i == len(maze):
            maze.append(['#']*len(maze[i-1]))
            maze[i][j] ='.'
        elif j == -1:
            for m in range(len(maze)):
                maze[m].insert(0,'#')
            j = 0
            maze[i][j] = '.'
        elif j == len(maze[i]):
            for m in range(len(maze)):
                maze[m].append('#')
            maze[i][j] = '.'
        else:
            maze[i][j] = '.'
for m in range(len(maze)):
    print(''.join(maze[m]))