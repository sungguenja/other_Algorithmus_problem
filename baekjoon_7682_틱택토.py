from sys import stdin
from collections import deque
input = stdin.readline

def checkCnt(status):
    O_cnt = 0
    X_cnt = 0
    for i in status:
        if i == 'O':
            O_cnt += 1
        elif i == 'X':
            X_cnt += 1
    return O_cnt,X_cnt

def checkFin(status):
    game = []
    for i in range(3):
        game.append(status[3*i:3*i+3])
        
    return bfs(game)
    
def bfs(game):
    di = [0,1,1,1,0,-1,-1,-1]
    dj = [1,1,0,-1,-1,-1,0,1]
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X' or game[i][j] == 'O':
                target = game[i][j]
                Que = deque()
                Que.append((i,j,1,123))
                visit = [[False]*3 for _ in range(3)]
                visit[i][j] = True
                while Que:
                    start_i,start_j,cnt,directioln = Que.popleft()
                    if cnt >= 3:
                        return True,target
                    for k in range(8):
                        ni = start_i + di[k]
                        nj = start_j + dj[k]
                        if 0<=ni<3 and 0<=nj<3 and not visit[ni][nj] and game[ni][nj] == target:
                            if directioln == 123:
                                visit[ni][nj] = True
                                Que.append((ni,nj,cnt+1,k))
                            elif directioln == k:
                                visit[ni][nj] = True
                                Que.append((ni,nj,cnt+1,k))
    return False, '.'

while True:
    now = input()
    if now == 'end' or now == 'end\n':
        break
    O_cnt, X_cnt = checkCnt(now)
    if O_cnt != X_cnt and O_cnt + 1 != X_cnt:
        print("invalid")
        continue
    is_win, who_win = checkFin(now)
    if is_win:
        if who_win == 'O':
            if O_cnt != X_cnt:
                print("invalid")
            else:
                print("valid")
        else:
            if O_cnt + 1 != X_cnt:
                print("invalid")
            else:
                print("valid")
    else:
        if '.' not in now:
            print("valid")
        else:
            print("invalid")