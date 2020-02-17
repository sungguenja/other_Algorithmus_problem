import copy

N,M = map(int,input().split())
direction =[[0,1],[1,0],[0,-1],[-1,0]]

room = []
lab = []
virus = []
for i in range(N):
    horizont = []
    horizont = list(map(int,input().split()))
    for j in range(M):
        if horizont[j] == 0:
            room.append([i,j])
        elif horizont[j] == 2:
            virus.append([i,j])
    lab.append(horizont)
copy_lab = [[0]*M for _ in range(N)]
for k in virus:
    copy_lab[k[0]][k[1]] = 1

save_copy = copy.deepcopy(copy_lab)
safe_room=0
for i in range(len(room)-2):
    for j in range(i+1,len(room)-1):
        for k in range(j+1,len(room)):
            copy_lab = copy.deepcopy(save_copy)
            copy_lab[room[i][0]][room[i][1]] = 1
            copy_lab[room[j][0]][room[j][1]] = 1
            copy_lab[room[k][0]][room[k][1]] = 1
            que = []
            for l in virus:
                que.append(l)
            while que != []:
                X=que.pop()
                ni,nj=X[0],X[1]
                for nk in direction:
                    if 0<=ni+nk[0]<N and 0<=nj+nk[1]<M:
                        if copy_lab[ni+nk[0]][nj+nk[1]] == 0 and lab[ni+nk[0]][nj+nk[1]] == 0:
                            que.append([ni+nk[0],nj+nk[1]])
                            copy_lab[ni+nk[0]][nj+nk[1]] = copy_lab[ni][nj] +1
            cnt = 0
            for x in range(M):
                for y in range(N):
                    if copy_lab[y][x] == 0 and lab[y][x] == 0:
                        cnt += 1
            if cnt > safe_room:
                safe_room = cnt
print(safe_room)