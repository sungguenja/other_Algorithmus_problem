from collections import deque
def setMirror(room,start,end,size):
    result = (size+1)**2
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[[-1]*4 for j in range(size)] for i in range(size)]
    Que = deque()
    Que.append((start[0],start[1],0,5))
    while Que:
        i,j,cost,direction = Que.popleft()
        if cost >= result:
            continue
        if i == end[0] and j == end[1]:
            if cost < result:
                result = cost
            continue
        for next_direction in range(4):
            ni = i + di[next_direction]
            nj = j + dj[next_direction]
            if 0<=ni<size and 0<=nj<size:
                if direction == 5:
                    if room[ni][nj] != '*':
                        if visit[ni][nj][next_direction] == -1 or visit[ni][nj][next_direction] > cost: 
                            visit[ni][nj][next_direction] = cost
                            Que.append((ni,nj,cost,next_direction))
                else:
                    if room[i][j] == '.':
                        if room[ni][nj] != '*' and direction == next_direction and (visit[ni][nj][next_direction] == -1 or visit[ni][nj][next_direction] > cost): 
                            visit[ni][nj][next_direction] = cost
                            Que.append((ni,nj,cost,next_direction))
                    elif room[i][j] == '!':
                        if room[ni][nj] != '*':
                            if direction == next_direction and (visit[ni][nj][next_direction] == -1 or visit[ni][nj][next_direction] > cost):
                                visit[ni][nj][next_direction] = cost
                                Que.append((ni,nj,cost,next_direction))
                            elif (direction + 2) % 4 != next_direction and (visit[ni][nj][next_direction] == -1 or visit[ni][nj][next_direction] > cost + 1):
                                visit[ni][nj][next_direction] = cost + 1
                                Que.append((ni,nj,cost+1,next_direction))
    return result

N = int(input())
start = []
end = []
room = [0]*N
for i in range(N):
    horizon = list(input())
    if start == [] or end == []:
        for j in range(N):
            if horizon[j] == '#':
                if start == []:
                    start = (i,j)
                else:
                    end = (i,j)
    room[i] = tuple(horizon[:])
room = tuple(room)
answer = setMirror(room,start,end,N)
print(answer)