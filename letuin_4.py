N = int(input())
maze = [list(map(int,input().split())) for i in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

start_i = 0
start_j = 0
direction = 0
left = 3
answer = 0

visit = [[False]*N for i in range(N)]
visit[0][0] = True

while start_i != N-1 or start_j != N-1:
    
    next_i = start_i + di[direction]
    next_j = start_j + dj[direction]
    left_i = start_i + di[left]
    left_j = start_j + dj[left]
    
    if 0<=next_i<N and 0<=next_j<N and maze[next_i][next_j] == 0:
        if left_i < 0 or left_i >= N or left_j < 0 or left_j >= N or maze[left_i][left_j] == 1:
            answer += 1
            start_i = next_i
            start_j = next_j
            visit[start_i][start_j] = True
        else:
            if visit[left_i][left_j] == False:
                direction = (direction - 1) % 4
                left = (direction - 1) % 4
            else:
                answer += 1
                start_i = next_i
                start_j = next_j
                visit[start_i][start_j] = True
    else:
        if left_i < 0 or left_i >= N or left_j < 0 or left_j >= N or maze[left_i][left_j] == 1:
            direction = (direction + 1)%4
            left = (direction - 1)%4
        else:
            direction = (direction - 1)%4
            left = (direction - 1)%4
        

print(answer)