N,M=map(int,input().split())
game = [list(input()) for i in range(N)]
answer = 0
di = [0,1,0,-1]
dj = [1,0,-1,0]
visit = [[0]*M for i in range(N)]
memoigation = [[-1]*M for i in range(N)]
def solution(i=0,j=0,cnt=1):
    global answer
    if answer == -1:
        return True

    if cnt>answer:
        answer = cnt
    visit[i][j] = 1
    memoigation[i][j] = cnt
    for k in range(4):
        ni = i + di[k]*int(game[i][j])
        nj = j + dj[k]*int(game[i][j])
        if 0<=ni<N and 0<=nj<M and game[ni][nj] != 'H':
            if visit[ni][nj] == 1:
                answer = -1
                return True
            if memoigation[ni][nj] != 0 and cnt < memoigation[ni][nj]:
                continue
            if solution(ni,nj,cnt+1):
                return True
    visit[i][j] = 0
    return False
solution()
print(answer)