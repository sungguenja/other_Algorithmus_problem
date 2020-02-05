wtf = list(map(int, input().split()))
N,M,K=wtf[0],wtf[1],wtf[4]
pan = []
for _ in range(N):
    pan_garo=[]
    pan_garo = list(map(int, input().split()))
    pan.append(pan_garo)
dice =[0,0,0,0,0,0]
dice_whe = [wtf[2],wtf[3]]
di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]
control = list(map(int, input().split()))
for k in control:
    dice_whe[0] += di[k]
    dice_whe[1] += dj[k]
    if dice_whe[0] < 0 or dice_whe[0] >= N or dice_whe[1] < 0 or dice_whe[1] >=M:
        dice_whe[0] -= di[k]
        dice_whe[1] -= dj[k]
        continue
    if k == 1:
        dice[0], dice[3], dice[2], dice[1] = dice[3], dice[2], dice[1], dice[0]
        if pan[dice_whe[0]][dice_whe[1]] == 0:
            pan[dice_whe[0]][dice_whe[1]] = dice[2]
        else:
            dice[2] = pan[dice_whe[0]][dice_whe[1]]
            pan[dice_whe[0]][dice_whe[1]] = 0
    if k == 2:
        dice[0], dice[3], dice[2], dice[1] = dice[1], dice[0], dice[3], dice[2]
        if pan[dice_whe[0]][dice_whe[1]] == 0:
            pan[dice_whe[0]][dice_whe[1]] = dice[2]
        else:
            dice[2] = pan[dice_whe[0]][dice_whe[1]]
            pan[dice_whe[0]][dice_whe[1]] = 0
    if k == 3:
        dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]
        if pan[dice_whe[0]][dice_whe[1]] == 0:
            pan[dice_whe[0]][dice_whe[1]] = dice[2]
        else:
            dice[2] = pan[dice_whe[0]][dice_whe[1]]
            pan[dice_whe[0]][dice_whe[1]] = 0
    if k == 4:
        dice[0], dice[4], dice[2], dice[5] = dice[5], dice[0], dice[4], dice[2]
        if pan[dice_whe[0]][dice_whe[1]] == 0:
            pan[dice_whe[0]][dice_whe[1]] = dice[2]
        else:
            dice[2] = pan[dice_whe[0]][dice_whe[1]]
            pan[dice_whe[0]][dice_whe[1]] = 0
    print(dice[0])