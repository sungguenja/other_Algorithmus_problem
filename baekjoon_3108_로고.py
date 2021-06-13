from collections import deque
def moveToCoordinatePlane(x):
    return 2*(int(x)+500)

def checkArea(y,x):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    Que = deque()
    Que.append((y,x))
    while Que:
        i,j = Que.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<2001 and 0<=nj<2001:
                if my_coordinate_plane[ni][nj] and not visit[ni][nj]:
                    visit[ni][nj] = True
                    Que.append((ni,nj))

N = int(input())
my_coordinate_plane = [[False]*2001 for i in range(2001)]
for t in range(N):
    x1,y1,x2,y2 = map(moveToCoordinatePlane,input().split())
    for i in range(y1,y2+1):
        my_coordinate_plane[i][x1] = True
        my_coordinate_plane[i][x2] = True
    for j in range(x1,x2+1):
        my_coordinate_plane[y1][j] = True
        my_coordinate_plane[y2][j] = True
visit = [[False]*2001 for i in range(2001)]

answer = 0
if my_coordinate_plane[1000][1000]:
    checkArea(1000,1000)
for i in range(2001):
    for j in range(2001):
        if my_coordinate_plane[i][j] and not visit[i][j]:
            answer += 1
            checkArea(i,j)

print(answer)