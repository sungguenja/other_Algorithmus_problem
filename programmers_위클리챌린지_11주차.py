from copy import deepcopy
from collections import deque
LENGTH = 110

def checkPositionOfRectangle(rectangle):
    coordinate_plain = [[1]*LENGTH for _ in range(LENGTH)]
    for rectan in rectangle:
        for i in range(2*rectan[0],2*rectan[2]+1):
            for j in range(2*rectan[1],2*rectan[3]+1):
                coordinate_plain[i][j] = 2
    return deepcopy(coordinate_plain)

def checkLine(plain):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[False]*LENGTH for _ in range(LENGTH)]
    Que = deque()
    Que.append((0,0))
    while Que:
        i,j = Que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<LENGTH and 0<=nj<LENGTH and not visit[ni][nj]:
                visit[ni][nj] = True
                if plain[ni][nj] == 1:
                    Que.append((ni,nj))
                else:
                    plain[ni][nj] = 0
    return deepcopy(plain)
        
def findShortestRoute(plain,start,end):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[False]*LENGTH for _ in range(LENGTH)]
    Que = deque()
    Que.append((start[0],start[1],0))
    answer = 51*51+3
    
    while Que:
        i,j,cost = Que.popleft()
        if cost>=answer:
            continue
        
        if i == end[0] and j == end[1]:
            if cost < answer:
                answer = cost
            continue
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<LENGTH and 0<=nj<LENGTH and not visit[ni][nj]:
                visit[ni][nj] = True
                if plain[ni][nj] == 0:
                    Que.append((ni,nj,cost+0.5))
    return answer
 
def makeRedeemPlain(plain,start):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[False]*LENGTH for _ in range(LENGTH)]
    Que = deque()
    Que.append((start[0],start[1]))
    
    while Que:
        i,j = Que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<LENGTH and 0<=nj<LENGTH and not visit[ni][nj]:
                visit[ni][nj] = True
                if plain[ni][nj] == 0:
                    Que.append((ni,nj))
                elif plain[ni][nj] == 2:
                    before_d = (k-1)%4
                    bi = i + di[before_d]
                    bj = j + dj[before_d]
                    after_d = (k+1)%4
                    ai = i + di[after_d]
                    aj = j + dj[after_d]
                    if (0<=bi<LENGTH and 0<=bj<LENGTH and plain[bi][bj] == 1) or (0<=ai<LENGTH and 0<=aj<LENGTH and plain[ai][aj] == 1):
                        plain[ni][nj] = 0
                        Que.append((ni,nj))
    return deepcopy(plain)
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    coordinate_plain = checkPositionOfRectangle(rectangle)
    checked_plain = checkLine(coordinate_plain)
    redeem_plain = makeRedeemPlain(coordinate_plain,(2*characterX, 2*characterY))
    answer = findShortestRoute(redeem_plain,(2*characterX, 2*characterY),(2*itemX, 2*itemY))
    return answer