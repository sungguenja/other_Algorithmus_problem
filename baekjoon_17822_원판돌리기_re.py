from collections import deque
N,M,T=map(int,input().split())
circle = [0]*N
for i in range(N):
    circle[i] = list(map(int,input().split()))
command = [0]*T
for i in range(T):
    command[i] = list(map(int,input().split()))

di = [0,1,0,-1]
dj = [1,0,-1,0]

for com in command:
    xi, ddi, ki = com[0], com[1], com[2]
    for i in range(N):
        if (i+1)%xi == 0:
            if ddi == 0:
                for k in range(ki):
                    circle[i].insert(0,circle[i].pop())
            else:
                for k in range(ki):
                    circle[i].append(circle[i].pop(0))
    trigger = False
    for i in range(N):
        for j in range(M):
            if circle[i][j] != 'x':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if nj<0:
                        nj += M
                    elif nj>=M:
                        nj -= M
                    if 0<=ni<N and 0<=nj<M and circle[i][j] == circle[ni][nj]:
                        trigger = True
                        break
            if trigger:
                break
        if trigger:
            break
    
    if trigger:
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 'x' and (circle[i][j] == circle[i][j-1] or (j+1<M and circle[i][j] == circle[i][j+1]) or (j+1 >= M and circle[i][j] == circle[i][0]) or (i-1>=0 and circle[i][j] == circle[i-1][j]) or (i+1<N and circle[i][j] == circle[i+1][j])):
                    Que = deque()
                    visit = [[0]*M for i in range(N)]
                    check = circle[i][j]
                    Que.append([i,j])
                    visit[i][j] = 1
                    circle[i][j] = 'x'
                    while Que:
                        ni,nj = Que.popleft()
                        for k in range(4):
                            nni = ni + di[k]
                            nnj = nj + dj[k]
                            if nnj<0:
                                nnj += M
                            elif nnj>=M:
                                nnj -= M
                            if 0<=nni<N and 0<=nnj<M and visit[nni][nnj] == 0 and circle[nni][nnj] == check:
                                circle[nni][nnj] = 'x'
                                visit[nni][nnj] = 1
                                Que.append([nni,nnj])
    else:
        cnt = 0
        check_sum = 0
        case = []
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 'x':
                    check_sum += circle[i][j]
                    cnt += 1
                    case.append([i,j])
        if cnt > 0:
            check_sum = check_sum/cnt
            for ca in case:
                i,j=ca[0],ca[1]
                if circle[i][j] < check_sum:
                    circle[i][j] += 1
                elif circle[i][j] > check_sum:
                    circle[i][j] -= 1

answer = 0
for i in range(N):
    for j in range(M):
        if circle[i][j] != 'x':
            answer += circle[i][j]
print(answer)
