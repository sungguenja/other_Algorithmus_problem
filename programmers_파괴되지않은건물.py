def solution(board, skill):
    answer = 0
    damage_board = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for now_situation in skill:
        is_deal,r1,c1,r2,c2,degree = now_situation
        if is_deal == 1:
            damage_board[r1][c1] -= degree
            damage_board[r1][c2+1] += degree
            damage_board[r2+1][c1] += degree
            damage_board[r2+1][c2+1] -= degree
        else:
            damage_board[r1][c1] += degree
            damage_board[r1][c2+1] -= degree
            damage_board[r2+1][c1] -= degree
            damage_board[r2+1][c2+1] += degree
    
    for i in range(len(damage_board)-1):
        for j in range(len(damage_board[i])-1):
            damage_board[i][j + 1] += damage_board[i][j]
    
    for j in range(len(damage_board[0]) - 1):
        for i in range(len(damage_board) - 1):
            damage_board[i + 1][j] += damage_board[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] + damage_board[i][j] > 0:
                answer += 1

    return answer