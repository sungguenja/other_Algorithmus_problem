N=5
board = [list(map(int,input().split())) for i in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
case = set()
def find(i,j,cnt,now):
    if cnt == 5:
        case.add(now)
        return
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<N and 0<=nj<N:
            find(ni,nj,cnt+1,now+str(board[ni][nj]))

for i in range(N):
    for j in range(N):
        find(i,j,0,str(board[i][j]))
print(len(case))