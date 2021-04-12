from collections import deque
import sys
di = [0,1,0,-1]
dj = [1,0,-1,0]
W,H = map(int,sys.stdin.readline().split())
answer = (H+1)*(W+1)
def solution(now,end,W,H):
    visit = [[[-1]*4 for j in range(W)] for i in range(H)]
    visit[now[0]][now[1]][0] = 0
    visit[now[0]][now[1]][1] = 0
    visit[now[0]][now[1]][2] = 0
    visit[now[0]][now[1]][3] = 0
    answer_cost = answer
    Que = deque()
    Que.append((now[0],now[1],5))
    while Que:
        i,j,direction = Que.popleft()
        if direction != 5 and visit[i][j][direction] >= answer_cost:
            continue
        
        if i==end[0] and j==end[1]:
            if visit[i][j][direction] < answer_cost:
                answer_cost = visit[i][j][direction]
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<H and 0<=nj<W and (visit[ni][nj][k] == -1 or visit[ni][nj][k] > visit[i][j][direction]) and (maze[ni][nj] == '.' or maze[ni][nj] == 'C'):
                if direction == 5:
                    visit[ni][nj][k] = visit[i][j][0]
                    Que.append((ni,nj,k))
                else:
                    if k == direction:
                        visit[ni][nj][k] = visit[i][j][direction]
                        Que.append((ni,nj,k)) # 직진
                    elif k == (direction+2)%4:
                        continue # 반대방향
                    else:
                        visit[ni][nj][k] = visit[i][j][direction] + 1 # 회전
                        Que.append((ni,nj,k))
    return answer_cost

maze = [0]*H
trigger = 0
start = []
end = []
for i in range(H):
    horizon = list(sys.stdin.readline())
    if trigger < 2:
        for j in range(W):
            if horizon[j] == 'C':
                if trigger == 0:
                    start = (i,j)
                else:
                    end = (i,j)
                trigger += 1
    maze[i] = horizon[:]
answer = solution(start,end,W,H)
print(answer)