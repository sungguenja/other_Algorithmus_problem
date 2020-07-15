from copy import deepcopy
direction = [0,[1,-1],[1,0],[1,1],[0,-1],[0,0],[0,1],[-1,-1],[-1,0],[-1,1]]
N,M = map(int,input().split())
crazy = []
jongsoo = []
board = [0]*N
for i in range(N):
    board[i] = list(input())
    for j in range(M):
        if board[i][j] == 'R':
            crazy.append([i,j])
        elif board[i][j] == 'I':
            jongsoo = [i,j]

command = list(map(int,list(input())))

end = False
cnt = 0
for com in range(len(command)):
    cnt+=1
    visit = [[0]*M for i in range(N)]
    board[jongsoo[0]][jongsoo[1]] = '.'

    jongsoo[0] += direction[command[com]][0]
    jongsoo[1] += direction[command[com]][1]

    if jongsoo in crazy:
        end = True
        break

    board[jongsoo[0]][jongsoo[1]] = 'I'
    before_crazy = deepcopy(crazy)

    for robot in crazy:
        if robot == 0:
            continue
        rich = N*M
        whe = 15
        for k in range(1,10):
            ni = robot[0] + direction[k][0]
            nj = robot[1] + direction[k][1]
            if 0<=ni<N and 0<=nj<M:
                if rich>abs(jongsoo[0]-ni)+abs(jongsoo[1]-nj):
                    rich = abs(jongsoo[0]-ni)+abs(jongsoo[1]-nj)
                    whe = k
        robot[0] += direction[whe][0]
        robot[1] += direction[whe][1]
        if robot == jongsoo:
            break
        visit[robot[0]][robot[1]] += 1
    
    for robot in before_crazy:
        if robot == 0:
            continue
        board[robot[0]][robot[1]] = '.'
    for robot in crazy:
        if robot == 0:
            continue
        board[robot[0]][robot[1]] = 'R'
    
    if jongsoo in crazy:
        end = True
        break

    for i in range(N):
        for j in range(M):
            if visit[i][j] >= 2:
                board[i][j] = '.'
                for k in range(len(crazy)):
                    if crazy[k] == [i,j]:
                        crazy[k] = 0

if end:
    print('kraj {0} '.format(cnt))
else:
    for k in board:
        print(''.join(k))