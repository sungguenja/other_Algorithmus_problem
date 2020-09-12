def solution(board, r, c):
    card_count = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_count += 1
    answer = 16**card_count
    visit = [[0]*4 for _ in range(4)]
    check = [[0]*4 for _ in range(4)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    def dfs(i,j,card,before,cnt=1):
        nonlocal answer
        if cnt>=answer:
            return
        if card <= 0:
            if cnt<answer:
                answer = cnt
            return
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            while 0<=ni<4 and 0<=nj<4 and board[ni][nj] != 0:
                ni += di[k]
                nj += dj[k]
            if not (0<=ni<4 and 0<=nj<4):
                ni -= di[k]
                nj -= dj[k]
            if before == 0:
                if board[ni][nj]==0 and visit[ni][nj]<card_count:
                    visit[ni][nj] += 1
                    dfs(ni,nj,card,board[ni][nj],cnt+1)
                    visit[ni][nj] -= 1
                elif board[ni][nj]!=0 and visit[ni][nj]<card_count:
                    visit[ni][nj]+=1
                    if before != 0:
                        if before == board[ni][nj]:
                            if check[ni][nj] == 0:
                                check[ni][nj] = 1
                                dfs(ni,nj,card-1,0,cnt+2)
                                check[ni][nj] = 0
                            else:
                                dfs(ni,nj,card,before,cnt+1)
                    else:
                        check[ni][nj] = 1
                        dfs(ni,nj,card-1,board[ni][nj],cnt+2)
                        check[ni][nj] = 0
                    visit[ni][nj] -= 1
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<4 and 0<=nj<4:
                pass
            else:
                continue
            if before == 0:
                if board[ni][nj]==0 and visit[ni][nj]<card_count:
                    visit[ni][nj] += 1
                    dfs(ni,nj,card,board[ni][nj],cnt+1)
                    visit[ni][nj] -= 1
                elif board[ni][nj]!=0 and visit[ni][nj]<card_count:
                    visit[ni][nj]+=1
                    if before != 0:
                        if before == board[ni][nj]:
                            if check[ni][nj] == 0:
                                check[ni][nj] = 1
                                dfs(ni,nj,card-1,0,cnt+2)
                                check[ni][nj] = 0
                            else:
                                dfs(ni,nj,card,before,cnt+1)
                    else:
                        check[ni][nj] = 1
                        dfs(ni,nj,card-1,board[ni][nj],cnt+2)
                        check[ni][nj] = 0
                    visit[ni][nj] -= 1
    dfs(r,c,card_count,board[r][c])
    return answer