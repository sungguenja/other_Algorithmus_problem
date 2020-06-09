from copy import deepcopy
def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    trigger = True
    before_board = deepcopy(board)
    while trigger:
        visit = [[False]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '.' and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    visit[i][j] = True
                    visit[i][j+1] = True
                    visit[i+1][j] = True
                    visit[i+1][j+1] = True
        for i in range(m):
            for j in range(n):
                if visit[i][j]:
                    board[i][j] = '.'
                    answer += 1
        pass_case = [False]*n
        for i in range(m-1,-1,-1):
            for j in range(n):
                if pass_case[j]:
                    continue
                if board[i][j] == '.':
                    for t in range(i-1,-1,-1):
                        if board[t][j] != '.':
                            board[t][j],board[i][j] = board[i][j],board[t][j]
                            break
                    else:
                        pass_case[j] = True
                        continue
        if before_board == board:
            trigger = False
        else:
            before_board = deepcopy(board)
    return answer

print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))