from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]
check_i = [0,1,1,1,0,-1,-1,-1]
check_j = [1,1,0,-1,-1,-1,0,1]
N=int(input())
board = [0]*N
trigger = True
goal_trigger = True
for i in range(N):
    horizon = list(input())
    board[i]=horizon[:]
    if trigger:
        if 'B' in horizon:
            if horizon.count('B') == 1:
                tree = [i+1,horizon.index('B'),1] # 서있으면 1
            else:
                tree = [i,horizon.index('B')+1,0] # 누워있으면 0
            trigger = False
    if goal_trigger:
        if 'E' in horizon:
            if horizon.count('E') == 1:
                goal = [i+1,horizon.index('E'),1]
            else:
                goal = [i,horizon.index('E')+1,0]
            goal_trigger = False
visit = [[[0]*2 for i in range(N)] for j in range(N)]
visit[tree[0]][tree[1]][tree[2]] = 1
answer = ((N+1)**2)*2
Que = deque()
Que.append([tree[0],tree[1],tree[2],0])
while Que:
    i,j,shape,cnt = Que.popleft()
    if cnt >= answer:
        continue
    
    if [i,j,shape] == goal:
        if answer > cnt:
            answer = cnt
        continue
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N:
            if visit[ni][nj][shape] == 0:
                if shape==0 and 0<=nj-1<N and 0<=nj+1<N and board[ni][nj]!='1' and board[ni][nj+1]!='1' and board[ni][nj-1]!='1':
                    visit[ni][nj][shape]=1
                    Que.append([ni,nj,shape,cnt+1])
                elif shape==1 and 0<=ni-1<N and 0<=ni+1<N and board[ni][nj]!='1' and board[ni-1][nj]!='1' and board[ni+1][nj]!='1':
                    visit[ni][nj][shape]=1
                    Que.append([ni,nj,shape,cnt+1])
    
    if visit[i][j][(shape+1)%2] == 0:
        for k in range(8):
            ni = i + check_i[k]
            nj = j + check_j[k]
            if ni<0 or ni>=N or nj<0 or nj>=N:
                break
            if board[ni][nj] == '1':
                break
        else:
            visit[i][j][(shape+1)%2] = 1
            Que.append([i,j,(shape+1)%2,cnt+1])

if answer==((N+1)**2)*2:
    answer = 0
print(answer)