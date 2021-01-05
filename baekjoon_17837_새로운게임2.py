N,K = map(int,input().split())
chess = [list(map(int,input().split())) for i in range(N)]
moving = [[0]*N for i in range(N)]
unit = []
di = [0,0,-1,1]
dj = [1,-1,0,0]
for k in range(K):
    i,j,d = map(int,input().split())
    unit.append([i-1,j-1,d-1,k])
    if moving[i-1][j-1] == 0:
        moving[i-1][j-1] = [k]
    else:
        moving[i-1][j-1].append(k)
trigger = False

for t in range(1001):
    for k in range(K):
        i,j,d,nk = unit[k]
        moving_unit = []
        while len(moving[i][j]) > 0:
            nnk = moving[i][j].pop()
            moving_unit.append(nnk)
            if moving[i][j] == []:
                moving[i][j] = 0
            if nnk == nk:
                break
        # 움직임
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<N and chess[ni][nj] != 2:
            if chess[ni][nj] == 1:
                moving_unit.reverse()
            if moving[ni][nj] == 0:
                moving[ni][nj] = []
            while len(moving_unit) > 0:
                nnk = moving_unit.pop()
                nd = d
                if nnk != nk:
                    nd = unit[nnk][2]
                unit[nnk] = [ni,nj,nd,nnk]
                moving[ni][nj].append(nnk)
            if len(moving[ni][nj]) >= 4:
                trigger = True
                break
        else:
            if d==0 or d==2:
                d+=1
            else:
                d-=1
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N and chess[ni][nj] != 2:
                if chess[ni][nj] == 1:
                    moving_unit.reverse()
                if moving[ni][nj] == 0:
                    moving[ni][nj] = []
                while len(moving_unit) > 0:
                    nnk = moving_unit.pop()
                    nd = d
                    if nnk != nk:
                        nd = unit[nnk][2]
                    unit[nnk] = [ni,nj,nd,nnk]
                    moving[ni][nj].append(nnk)
                if len(moving[ni][nj]) >= 4:
                    trigger = True
                    break
            else:
                if moving[i][j] == 0:
                    moving[i][j] = []
                while len(moving_unit) > 0:
                    nnk = moving_unit.pop()
                    nd = d
                    if nnk != nk:
                        nd = unit[nnk][2]
                    unit[nnk] = [i,j,nd,nnk]
                    moving[i][j].append(nnk)
                if len(moving[i][j]) >= 4:
                    trigger = True
                    break
    for k in range(K):
        i,j,d,nk = unit[k]
        if moving[i][j] != 0 and len(moving[i][j]) >= 4:
            trigger = True
            break
    if trigger:
        break

answer = t+1
if answer >= 1000:
    answer = -1

print(answer)