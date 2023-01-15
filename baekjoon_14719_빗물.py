h, w = map(int,input().split())
board = list(map(int,input().split()))

answer = 0
for i in range(1,w-1):
    left_wall = max(board[:i])
    right_wall = max(board[i+1:])

    lower_wall = min(left_wall,right_wall)
    
    if (board[i] < lower_wall):
        answer += lower_wall - board[i]

print(answer)