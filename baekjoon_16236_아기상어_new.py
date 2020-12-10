from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]
N = int(input())
# 물고기 저장용
fishes = {1:[],2:[],3:[],4:[],5:[],6:[]}
size = 2
eat_cnt = 0
aqua = [0]*N
for i in range(N):
    horizon = list(map(int,input().split()))
    for j in range(N):
        if horizon[j] == 9:
            shark = [i,j]
            horizon[j] = 0
        elif horizon[j] in fishes.keys():
            fishes[horizon[j]].append([i,j])
    aqua[i] = horizon[:]

d = (N+1)**2
target_fish = [0,0]
# 물고기 거리 체크 용
def distance(si,sj,fi,fj,ss,fs,fw):
    global d,target_fish
    Que = deque()
    Que.append([si,sj,0])
    visit = [[0]*N for i in range(N)]
    while Que:
        i,j,cost = Que.popleft()
        if cost>d:
            continue
        if i==fi and j==fj:
            if cost<d:
                d=cost
                target_fish = [fi,fj,fs,fw]
            elif cost == d:
                if target_fish == []:
                    target_fish = [fi,fj,fs,fw]
                elif target_fish[0]>fi:
                    target_fish = [fi,fj,fs,fw]
                elif target_fish[0] == fi:
                    if target_fish[1] > fj:
                        target_fish = [fi,fj,fs,fw]
            continue
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == 0 and aqua[ni][nj]<=ss:
                visit[ni][nj] = 1
                Que.append([ni,nj,cost+1])
answer = 0
while True:
    cnt = 0
    d = (N+1)**2
    target_fish = []
    for i in range(1,7):
        if i>=size:
            break
        if fishes[i] == []:
            cnt += 1
            continue
        for j in range(len(fishes[i])):
            distance(shark[0],shark[1],fishes[i][j][0],fishes[i][j][1],size,i,j)
    if cnt == size:
        break
    if target_fish == []:
        break
    eat_cnt += 1
    aqua[target_fish[0]][target_fish[1]] = 0
    fishes[target_fish[2]].pop(target_fish[3])
    shark = [target_fish[0],target_fish[1]]
    if eat_cnt == size:
        size += 1
        eat_cnt = 0
    answer += d
print(answer)