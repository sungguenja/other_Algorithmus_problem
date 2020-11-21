from collections import deque
def solution(board):
    size = len(board)
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[0]*size for i in range(size)]
    Que = deque()
    Que.append([0,0,0,0])
    Que.append([0,0,1,0])
    while len(Que) != 0:
        i,j,d,cost = Que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<size and 0<=nj<size:
                if board[ni][nj] == 0:
                    if k==d:
                        if visit[ni][nj]==0 or visit[ni][nj]>=cost+100:
                            visit[ni][nj] = cost+100
                            Que.append([ni,nj,k,cost+100])
                    else:
                        if visit[ni][nj]==0 or visit[ni][nj]>=cost+600:
                            visit[ni][nj] = cost+600
                            Que.append([ni,nj,k,cost+600])
    return visit[-1][-1]