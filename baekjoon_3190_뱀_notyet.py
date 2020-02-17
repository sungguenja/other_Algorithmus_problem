N=int(input())
dummy = [[0]*N for _ in range(N)]
for _ in range(int(input())):
    apple1, apple2 = map(int,input().split())
    dummy[apple1-1][apple2-1] = 'A'

M=int(input())
command = [0]*M
for i in range(M):
    command[i] = list(input().split())

direction = [[0,1],[1,0],[0,-1],[-1,0]]
snake=[[0,0],[0,0]]
k=0
ending = 0
alive = 0
for i in range(M):
    for _ in range(int(command[i][0])):
        snake[0][0] += direction[k][0]
        snake[0][1] += direction[k][1]
        alive += 1
        if snake[0][0] >= N or snake[0][0] < 0 or snake[0][1] >= N or snake[0][1] < 0:
            ending = 1
            break
        if dummy[snake[0][0]][snake[0][1]] == 'A':
            dummy[snake[0][0]][snake[0][1]] = 0
            snake[1][0] += direction[k][0]
            snake[1][1] += direction[k][1]
    else:
        if command[i][1] == 'D':
            k = (k+1)%4
        elif command[i][1] == 'L':
            k = (k+3)%4
    if ending == 1:
        break
print(alive)