N=int(input())
d = N**2
direction = [[-1,0],[0,-1],[0,1],[1,0]]
trigger = False
def distance(si,sj,fi,fj,size,dis=0):
    global d, trigger
    if dis>=d:
        return

    if si==fi and sj==fj:
        trigger = True
        aqua[si][sj]=9
        if dis<d:
            d=dis
        return

    for k in range(4):
        ni,nj=si+direction[k][0],sj+direction[k][1]
        if 0<=ni<N and 0<=nj<N:
            if visit[ni][nj]==0 and (aqua[ni][nj]<=size or aqua[ni][nj]==9):
                visit[ni][nj] = 1
                distance(ni,nj,fi,fj,size,dis+1)
                visit[ni][nj] = 0

aqua = []
fish = {}
fishes = [1,2,3,4,5,6]
for i in range(N):
    horizon=[]
    horizon=list(map(int,input().split()))
    for j in range(N):
        if horizon[j]==9:
            shark = [i,j,2]
            horizon[j]=0
            break
        elif horizon[j] in fishes:
            if horizon[j] not in fish.keys():
                fish[horizon[j]] = [[i,j]]
            else:
                fish[horizon[j]].append([i,j])
    aqua.append(horizon)

cnt = 0
length = 0
while True:
    if shark[2]<=7:
        for i in range(1,shark[2]):
            if i in fish.keys():
                break
        else:
            break
    else:
        for i in range(1,7):
            if i in fish.keys():
                break
        else:
            break
    d = N**2
    fi,fj,what_f,whe_f=-1,-1,-1,-1
    trigger = False
    visit = [[0]*N for _ in range(N)]
    now_size = shark[2]
    if now_size>7:
        now_size = 7
    for i in range(1,now_size):
        for j in range(len(fish[i])):
            fish_dis = (abs(fish[i][j][0]-shark[0])+abs(fish[i][j][1]-shark[1]))
            if d>fish_dis:
                d = fish_dis
                fi,fj = fish[i][j][0],fish[i][j][1]
                what_f,whe_f=i,j
            elif d==fish_dis:
                if fi>fish[i][j][0]:
                    fi,fj = fish[i][j][0],fish[i][j][1]
                    what_f,whe_f=i,j
                elif fi == fish[i][j][0]:
                    if fj>fish[i][j][1]:
                        fi,fj = fish[i][j][0],fish[i][j][1]
                        what_f,whe_f=i,j
    d = N**2
    distance(shark[0],shark[1],fi,fj,shark[2])
    if trigger:
        aqua[shark[0]][shark[1]] = 0
        length += d
        cnt += 1
        if cnt == shark[2]:
            shark[2] += 1
            cnt = 0
        shark[0],shark[1]=fi,fj
        fish[what_f].pop(whe_f)
    else:
        break
    print('----------')
    for k in aqua:
        print(k)
    print(shark[2],length)
print(length)