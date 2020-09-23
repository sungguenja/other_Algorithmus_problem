import sys
sys.setrecursionlimit(10000)
di = [0,1,0,-1]
dj = [1,0,-1,0]
N,M=map(int,input().split())
load = [list(map(int,input().split())) for i in range(N)]
Que = [[0,0]]
memoization = [[-1]*M for i in range(N)]
def solution(i=0,j=0):
    if i == N-1 and j == M-1:
        return 1
    if memoization[i][j] != -1:
        return memoization[i][j]
    memoization[i][j]=0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M and load[i][j]>load[ni][nj]:
            memoization[i][j] += solution(ni,nj)
    return memoization[i][j]
print(solution())