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
for com in command:
    cnt+=1
    visit = [[0]*M for i in range(N)]
    board[jongsoo[0]][jongsoo[1]] = '.'
    jongsoo[0] += direction[com][0]
    jongsoo[1] += direction[com][1]
    if jongsoo in crazy:
        end = True
        break
    board[jongsoo[0]][jongsoo[1]] = 'I'
    for robot in crazy:
        board[robot[0]][robot[1]] = '.'
        if robot[0] > jongsoo[0]:
            robot[0] -= 1
            if robot[1] < jongsoo[1]:
                robot[1] += 1
            elif robot[1] > jongsoo[1]:
                robot[1] -= 1
        elif robot[0] == jongsoo[0]:
            if robot[1] < jongsoo[1]:
                robot[1] += 1
            elif robot[1] > jongsoo[1]:
                robot[1] -= 1
        else:
            robot[0] += 1
            if robot[1] < jongsoo[1]:
                robot[1] += 1
            elif robot[1] > jongsoo[1]:
                robot[1] -= 1
        visit[robot[0]][robot[1]] += 1
        board[robot[0]][robot[1]] = 'R'
    
    if jongsoo in crazy:
        end = True
        break

    for i in range(N):
        for j in range(M):
            if visit[i][j] >= 2:
                k = 0
                while k<len(crazy):
                    if crazy[k] == [i,j]:
                        crazy.pop(k)
                    else:
                        k+=1
                board[i][j] = '.'

if end:
    print('kraj {0}'.format(cnt))
else:
    for k in board:
        print(''.join(k))