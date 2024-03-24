from collections import deque

def solution(board):
    answer = len(board)*len(board[0])*2
    solutionMaximum = len(board)*len(board[0])*2
    visitBoard = [[solutionMaximum]*len(board[0]) for _ in range(len(board))]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    Que = deque()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                Que.append([i,j,0])
                visitBoard[i][j] = 0

    while Que:
        i,j,cnt = Que.popleft()
        if (board[i][j] == 'G'):
            if answer >= cnt:
                answer = cnt
            continue

        for k in range(4):
            ni = i
            nj = j
            while 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != 'D':
                ni += di[k]
                nj += dj[k]
            ni -= di[k]
            nj -= dj[k]
            if (visitBoard[ni][nj] > cnt + 1):
                visitBoard[ni][nj] = cnt + 1
                Que.append([ni,nj,cnt+1])
    
    if answer == solutionMaximum:
        answer = -1
    return answer