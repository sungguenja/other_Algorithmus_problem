from collections import deque
from copy import deepcopy

def bfs(board,visit,is_blind,start):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    Que = deque()
    Que.append(start)
    while Que:
        i,j = Que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni < N and 0<= nj <N and not visit[ni][nj]:
                if board[ni][nj] == board[i][j] or (is_blind and (board[ni][nj] == 'G' or board[ni][nj] == 'R') and (board[i][j] == 'R' or board[i][j] == 'G')):
                    visit[ni][nj] = True
                    Que.append([ni,nj])
    return deepcopy(visit)

def findDifferencePlaceCount(N,board,visit,is_blind=False):
    answer = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                answer += 1
                visit[i][j] = True
                visit = bfs(board,visit,is_blind,[i,j])
    return answer

N = int(input())
greed = [list(input()) for _ in range(N)]

visit_normal = [[False]*N for _ in range(N)]
visit_color_blind = [[False]*N for _ in range(N)]
normal_count = findDifferencePlaceCount(N,greed,visit_normal)
blind_count = findDifferencePlaceCount(N,greed,visit_color_blind,True)
print(normal_count,blind_count)