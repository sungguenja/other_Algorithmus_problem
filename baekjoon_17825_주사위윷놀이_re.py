from copy import deepcopy
board = [
    [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0],
    [10,13,16,19,25,30,35,40,0],
    [20,22,24,25,30,35,40,0],
    [30,28,27,26,25,30,35,40,0],
    [40,0]
]

check_list = [16,22,24,26,28,25,30]

dice = list(map(int,input().split()))

answer = 0

def solution(now=0,cost=0,position=[[0,0],[0,0],[0,0],[0,0]]):
    global answer
    if now>=10:
        if cost>answer:
            answer = cost
        return
    
    for k in range(4):
        i = position[k][0]
        j = position[k][1]
        if j>0 and (j>=len(board[i]) or board[i][j] == 0):
            continue
        nj = j + dice[now]
        if nj>=len(board[i]):
            n_position = deepcopy(position)
            n_position[k] = [i,len(board[i])][:]
            solution(now+1,cost,n_position)
        else:
            n_position = deepcopy(position)
            if i == 0 and board[i][nj] % 10 == 0 and board[i][nj] != 0:
                if (i==1 and nj==5) or (i==2 and nj==4) or (i==3 and nj==5):
                    trigger = True
                    for t in range(4):
                        if t==k:
                            continue
                        ci = position[t][0]
                        cj = position[t][1]
                        if cj >= len(board[ci]):
                            continue
                        if board[ci][cj] != 0 and board[i][nj] != 0 and board[ci][cj] == board[i][nj]:
                            if (board[ci][cj] in check_list) and (board[i][nj] in check_list):
                                if ci==i and cj==nj:
                                    trigger = False
                                    break
                            else:
                                trigger = False
                                break
                    if trigger:
                        if [i,nj] not in n_position:
                            n_position[k] = [i,nj][:]
                            solution(now+1,cost+board[i][nj],n_position)
                        if position.count([i,j]) >= 2:
                            break
                else:
                    ni = board[i][nj] // 10
                    trigger = True
                    for t in range(4):
                        if t==k:
                            continue
                        ci = position[t][0]
                        cj = position[t][1]
                        if cj >= len(board[ci]):
                            continue
                        if board[ci][cj] != 0 and board[ni][0] != 0 and board[ci][cj] == board[ni][0]:
                            if board[ci][cj] == 30 and board[ni][0] == 30:
                                if ci == ni and cj == nj:
                                    trigger = False
                                    break
                            else:
                                trigger = False
                                break
                    if trigger:
                        if [ni,0] not in n_position:
                            n_position[k] = [ni,0][:]
                            solution(now+1,cost+board[ni][0],n_position)
                        if position.count([i,j]) >= 2:
                            break
            else:
                trigger = True
                for t in range(4):
                    if t==k:
                        continue
                    ci = position[t][0]
                    cj = position[t][1]
                    if cj >= len(board[ci]):
                        continue
                    if board[ci][cj] != 0 and board[i][nj] != 0 and board[ci][cj] == board[i][nj]:
                        if (board[ci][cj] in check_list) and (board[i][nj] in check_list):
                            if ci==i and cj==nj:
                                trigger = False
                                break
                        else:
                            trigger = False
                            break
                if trigger:
                    if [i,nj] not in n_position:
                        n_position[k] = [i,nj][:]
                        solution(now+1,cost+board[i][nj],n_position)
                    if position.count([i,j]) >= 2:
                        break
solution()
print(answer)