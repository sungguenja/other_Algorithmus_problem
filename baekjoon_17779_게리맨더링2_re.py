def makeBoard(x,y,d1,d2,N):
    tmpBoard = [[0]*N for _ in range(N)]
    for i in range(d1):
        tmpBoard[x + i][y - i] = 5
    for i in range(1, d2+1):
        tmpBoard[x + i][y + i] = 5
    for i in range(d2+1):
        tmpBoard[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1+1):
        tmpBoard[x + d2 + i][y + d2 - i] = 5
    return tmpBoard

N = int(input())
board = [list(map(int,input().split())) for i in range(N)]
answer = 100000*N*N

for i in range(N):
    for j in range(N):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 0 <= i - d1 < N and 0 <= i + d1 < N and 0 <= j - d2 < N and 0<= j + d2 < N:
                    numberBoard = makeBoard(i,j,d1,d2,N)
                    scoreBoard = [0,0,0,0,0]
                    for x in range(N):
                        for y in range(N):
                            if numberBoard[y][x] == 5:
                                scoreBoard[4] += board[y][x]
                            elif 0 <= y < i+d1 and 0 <= x < j:
                                scoreBoard[0] += board[y][x]
                            elif 0 <= y <= i+d2 and j < x < N:
                                scoreBoard[1] += board[y][x]
                            elif i+d1 <= y < N and 0 <= x < j-d1+d2:
                                scoreBoard[2] += board[y][x]
                            elif i+d2 <= y < N and j-d1+d2 <= x < N:
                                scoreBoard[3] += board[y][x]
                    if max(scoreBoard) - min(scoreBoard) > answer:
                        answer = max(scoreBoard) - min(scoreBoard)

print(answer)