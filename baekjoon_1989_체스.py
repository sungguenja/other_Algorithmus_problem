N,M = map(int,input().split())
queens = list(map(int,input().split()))
knights = list(map(int,input().split()))
pawns = list(map(int,input().split()))
chess = [[0]*M for i in range(N)]
for k in range(1,len(queens),2):
    i,j=queens[k],queens[k+1]
    chess[i-1][j-1] = 'Q'
for k in range(1,len(knights),2):
    i,j=knights[k],knights[k+1]
    chess[i-1][j-1] = 'K'
for k in range(1,len(pawns),2):
    i,j=pawns[k],pawns[k+1]
    chess[i-1][j-1] = 'P'
knights_moving = [[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2]]
queens_moving = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
answer = 0
for k in range(1,len(knights),2):
    i,j=knights[k],knights[k+1]
    i -= 1
    j -= 1
    for km in knights_moving:
        ni = i+km[0]
        nj = j+km[1]
        if 0<=ni<N and 0<=nj<M and chess[ni][nj] == 0:
            chess[ni][nj] = -1
for q in range(1,len(queens),2):
    i,j=queens[q],queens[q+1]
    i -= 1
    j -= 1
    for qm in queens_moving:
        ni = i+qm[0]
        nj = j+qm[1]
        while 0<=ni<N and 0<=nj<M and (chess[ni][nj] == 0 or chess[ni][nj] == -1):
            chess[ni][nj] = -1
            ni += qm[0]
            nj += qm[1]
for i in range(N):
    for j in range(M):
        if chess[i][j] == 0:
            answer += 1
print(answer)