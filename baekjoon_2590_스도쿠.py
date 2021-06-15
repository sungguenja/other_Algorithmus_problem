from sys import stdin

input = stdin.readline
board = []
zero_list = []

for i in range(9):
    horizon = list(map(int,input().split()))
    for j in range(9):
        if horizon[j] == 0:
            zero_list.append((i,j))
    board.append(horizon)

answer = []
goal = len(zero_list)

def solveSudoku(goal,now=0):
    global answer
    if answer != []:
        return

    if now == goal:
        answer = board
        return
    
    can_put = [False]*9
    for i in range(9):
        if board[i][zero_list[now][1]] != 0:
            can_put[board[i][zero_list[now][1]]-1] = True
        if board[zero_list[now][0]][i] != 0:
            can_put[board[zero_list[now][0]][i]-1] = True

    start_i = (zero_list[now][0]//3)*3
    start_j = (zero_list[now][1]//3)*3
    for i in range(start_i,start_i+3):
        for j in range(start_j,start_j+3):
            if board[i][j] != 0:
                can_put[board[i][j]-1] = True
    
    cnt = 0
    can_go = []
    for k in range(9):
        if not can_put[k]:
            cnt += 1
            can_go.append(k+1)
    
    if cnt == 0:
        return

    for can in can_go:
        board[zero_list[now][0]][zero_list[now][1]] = can
        solveSudoku(goal,now+1)
        if answer != []:
            return
        board[zero_list[now][0]][zero_list[now][1]] = 0

solveSudoku(goal)
for k in answer:
    print(" ".join(map(str,k)))