def solution(board):
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    answer = 0
    N=len(board)
    right = direction[0]
    left = direction[2]
    up = direction[3]
    down = direction[1]
    Que = [[0,0,0,None,[[0,0]]]]
    visit = [[0]*N for _ in range(N)]
    visit[0][0] = 1
    while Que != []:
        now = Que.pop(0)
        i,j,cost,arrow,root = now[0],now[1],now[2],now[3],now[4]
        if i==N-1 and j==N-1:
            if answer==0 or answer>cost:
                answer = cost
            continue
        for k in direction:
            ni = i+k[0]
            nj = j+k[1]
            if (0<=ni<N and 0<=nj<N) and (board[ni][nj] == 0) and ([ni,nj] not in root) and (visit[ni][nj] < 64):
                if arrow == None:
                    if ni == 1 and nj == 0:
                        visit[ni][nj]+=1
                        Que.append([ni,nj,cost+100,down,root+[[ni,nj]]])
                    elif ni == 0 and nj == 1:
                        visit[ni][nj]+=1
                        Que.append([ni,nj,cost+100,right,root+[[ni,nj]]])

                elif arrow == right:
                    if k==right:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+100,right,root+[[ni,nj]]])
                    elif k==down:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,down,root+[[ni,nj]]])
                    elif k==up:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,up,root+[[ni,nj]]])

                elif arrow == down:
                    if k==down:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+100,down,root+[[ni,nj]]])
                    elif k==right:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,right,root+[[ni,nj]]])
                    elif k==left:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,left,root+[[ni,nj]]])

                elif arrow == left:
                    if k==up:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,up,root+[[ni,nj]]])
                    elif k==down:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,down,root+[[ni,nj]]])
                    elif k==left:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+100,left,root+[[ni,nj]]])

                elif arrow == up:
                    if k==left:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,left,root+[[ni,nj]]])
                    elif k==right:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+600,right,root+[[ni,nj]]])
                    elif k==up:
                        visit[ni][nj] += 1
                        Que.append([ni,nj,cost+100,up,root+[[ni,nj]]])

    return answer

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))