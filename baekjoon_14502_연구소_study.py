from copy import deepcopy
direction = [[0,1],[1,0],[0,-1],[-1,0]]
N,M = map(int,input().split())
lab = [0]*N
room = []
que = []
for i in range(N):
    lab[i] = list(map(int,input().split()))
    for j in range(M):
        if lab[i][j] == 0:
            room.append([i,j])
        elif lab[i][j] == 2:
            que.append([i,j])

answer = 0
for i in range(len(room)-2):
    for j in range(i+1,len(room)-1):
        for k in range(j+1,len(room)):
            visit = [[False]*M for _ in range(N)]
            copy_lab = deepcopy(lab)
            copy_lab[room[i][0]][room[i][1]] = 1
            copy_lab[room[j][0]][room[j][1]] = 1
            copy_lab[room[k][0]][room[k][1]] = 1
            copy_que = deepcopy(que)
            while copy_que != []:
                ni,nj=copy_que.pop(0)
                for d in direction:
                    nni = ni + d[0]
                    nnj = nj + d[1]
                    if 0<=nni<N and 0<=nnj<M:
                        if not visit[nni][nnj] and copy_lab[nni][nnj] == 0:
                            copy_lab[nni][nnj] = 2
                            visit[nni][nnj] = True
                            copy_que.append([nni,nnj])
            cnt = 0
            for ni in range(N):
                for nj in range(M):
                    if copy_lab[ni][nj] == 0:
                        cnt+=1
            if answer<cnt:
                answer=cnt
print(answer)