N = int(input())
board = [list(map(int,input().split())) for i in range(N)]
memo = [[-1]*N for i in range(N)]
visit = [[0]*N for i in range(N)]
di = [0,1]
dj = [1,0]
def memoization(i=0,j=0):
    if i==N-1 and j==N-1:
        return 1
    if visit[i][j] == 1:
        return memo[i][j]
    visit[i][j]=1
    memo[i][j]=0
    for k in range(2):
        ni = i+board[i][j]*di[k]
        nj = j+board[i][j]*dj[k]
        if 0<=ni<N and 0<=nj<N:
            memo[i][j] += memoization(ni,nj)

    return memo[i][j]

print(memoization())