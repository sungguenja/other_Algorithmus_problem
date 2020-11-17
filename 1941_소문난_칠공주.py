party = [list(input()) for i in range(5)]
answer = 0
visit = [[0]*5 for i in range(5)]
direction = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(n=-1,cnt=0,Spart=0,now_i=0,now_j=0):
    global answer
    if cnt==7:
        if Spart>=4:
            now_cnt = 1
            check_visit = [[0]*5 for i in range(5)]
            check_visit[now_i][now_j] = 1
            Que = [[now_i,now_j]]
            while Que:
                ni,nj = Que.pop(0)
                for k in range(4):
                    nni=ni+direction[k][0]
                    nnj=nj+direction[k][1]
                    if 0<=nni<5 and 0<=nnj<5 and check_visit[nni][nnj]==0 and visit[nni][nnj] == 1:
                        check_visit[nni][nnj]=1
                        now_cnt += 1
                        Que.append([nni,nnj])
            if now_cnt == 7:
                answer += 1
        return
    
    for i in range(n+1,25):
        ni = i//5
        nj = i%5
        if visit[ni][nj] == 0:
            visit[ni][nj] = 1
            if party[ni][nj] == 'S':
                dfs(i,cnt+1,Spart+1,ni,nj)
            else:
                dfs(i,cnt+1,Spart,ni,nj)
            visit[ni][nj] = 0
dfs()
print(answer)