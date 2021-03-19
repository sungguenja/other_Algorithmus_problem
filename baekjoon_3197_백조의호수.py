from collections import deque
from copy import deepcopy
R,C = map(int,input().split())
lake = [list(input()) for i in range(R)]
swan_first = []
swan_secon = []
trigger = 0
now_ice_que = deque()
next_ice_que = deque()
next_swan_que = deque()
di = [0,1,0,-1]
dj = [1,0,-1,0]
for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            if trigger == 0:
                swan_first = [i,j]
            elif trigger == 1:
                swan_secon = [i,j]
            trigger += 1
        elif lake[i][j] == ".":
            now_ice_que.append((i,j))
next_swan_que.append(swan_first)
t = 0

def meeting():
    global next_swan_que
    Que = deepcopy(next_swan_que)
    next_swan_que = deque()
    visit = [[False]*C for i in range(R)]

    while Que:
        i,j = Que.popleft()
        if [i,j] == swan_secon:
            return True
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<R and 0<=nj<C and visit[ni][nj] == False:
                if lake[ni][nj] == ".":
                    visit[ni][nj] = True
                    Que.append((ni,nj))
                elif lake[ni][nj] == "L":
                    if [ni,nj] == swan_secon:
                        return True
                    else:
                        Que.append((ni,nj))
                else:
                    next_swan_que.append((ni,nj))
    return False

def erase_ice():
    global next_ice_que
    Que = deepcopy(next_ice_que)
    next_ice_que = deque()
    visit = [[False]*C for i in range(R)]

    while Que:
        i,j = Que.popleft()
        lake[i][j] = "."
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<R and 0<=nj<C and visit[ni][nj] == False:
                if lake[ni][nj] == "X":
                    next_ice_que.append((ni,nj))
                    

while True:
    if meeting():
        print(t)
        break
    else:
        erase_ice()
        t += 1