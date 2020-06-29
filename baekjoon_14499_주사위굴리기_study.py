dice = [0,0,0,0,0,0]
# 0: 북 1: 서 2: 위 3: 동 4: 남 5: 바닥
di = [0,0,-1,1]
dj = [1,-1,0,0]
N,M,X,Y,K = map(int,input().split())
game = []
for i in range(N):
    game.append(list(map(int,input().split())))
commend = list(map(int,input().split()))
i,j = X,Y
for commend_cnt in range(K):
    now = commend[commend_cnt]
    ni = i + di[now-1]
    nj = j + dj[now-1]
    if ni>=N or ni<0 or nj>=M or nj<0:
        continue
    i = ni
    j = nj
    if now == 1:
        dice[1],dice[2],dice[3],dice[5] = dice[5],dice[1],dice[2],dice[3]
    elif now == 2:
        dice[1],dice[2],dice[3],dice[5] = dice[2],dice[3],dice[5],dice[1]
    elif now == 3:
        dice[0],dice[2],dice[4],dice[5] = dice[2],dice[4],dice[5],dice[0]
    elif now == 4:
        dice[0],dice[2],dice[4],dice[5] = dice[5],dice[0],dice[2],dice[4]
    
    if game[i][j] == 0:
        game[i][j] = dice[5]
    else:
        dice[5] = game[i][j]
        game[i][j] = 0
    print(dice[2])