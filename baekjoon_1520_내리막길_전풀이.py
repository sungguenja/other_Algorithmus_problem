import sys
sys.setrecursionlimit(10000)
di = [0,1,0,-1]
dj = [1,0,-1,0]
N,M=map(int,input().split())
load = [list(map(int,input().split())) for i in range(N)]
Que = [[0,0]]
visit = [[0]*M for i in range(N)]
memoization = [[0]*M for i in range(N)]
memoization[-1][-1] = 1
def solution(i=0,j=0):
    if i == N-1 and j == M-1:
        return
    visit[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M and load[i][j]>load[ni][nj]:
            if visit[ni][nj] == 0:
                if memoization[ni][nj] == 0:
                    solution(ni,nj)
            memoization[i][j] += memoization[ni][nj]
        print('--------')
        for k in memoization:
            print(k)
solution()
print(memoization[0][0])