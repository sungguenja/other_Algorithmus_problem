R, C, T = map(int, input().split())
di = [0,1,0,-1]                        # 미세먼지 확산용
dj = [1,0,-1,0]
room = [['B']*(C+2)]                                # 벽만들기
for _ in range(R):
    garo = []
    garo = ['B']+list(map(int, input().split()))+['B']  # 앞뒤로 벽
    room.append(garo)
room.append(['B']*(C+2))                            # 맨 밑에 벽

where_clean = []
for i in range(1,R+1):
    if len(where_clean) == 2:
        break
    for j in range(1, C+1):
        if room[i][j] == -1:
            where_clean = [i,j]
            break

for _ in range(T):         # 어차피 안쓰이는 변수라 _로 둠 횟수만 돌릴 생각
    dust_save = [[0]*(C+2)]
    for t in range(R):
        dust_garo = []
        dust_garo = [0]*(C+2)
        dust_save.append(dust_garo)
    dust_save.append([0]*(C+2))
    for i in range(1,R+1):  # 미세먼지 확산 저장
        for j in range(1,C+1):
            cnt = 0
            if room[i][j] != 0 and room[i][j] != -1:
                for k in range(4):
                    if room[i+di[k]][j+dj[k]] == 'B' or room[i+di[k]][j+dj[k]] == -1:
                        continue
                    else:
                        dust_save[i+di[k]][j+dj[k]] += room[i][j]//5
                        cnt += 1
                room[i][j] -= (room[i][j]//5)*cnt
    for i in range(1,R+1):      # 미세먼지 확산 결과
        for j in range(1,C+1):
            room[i][j] += dust_save[i][j]
    for i in range(where_clean[0]-1,1,-1):  #공기청정기 상부
        room[i][where_clean[1]] = room[i-1][where_clean[1]]
        room[i-1][where_clean[1]] = 0
    for j in range(where_clean[1],C):
        room[1][j] = room[1][j+1]
        room[1][j+1] = 0
    for i in range(1,where_clean[0]):
        room[i][C] = room[i+1][C]
        room[i+1][C] = 0
    for j in range(C,where_clean[1]+1,-1):
        room[where_clean[0]][j] = room[where_clean[0]][j-1]
        room[where_clean[0]][j-1] = 0
    
    for i in range(where_clean[0]+2,R+1):  #공기청정기 하부
        room[i][where_clean[1]] = room[i+1][where_clean[1]]
        room[i+1][where_clean[1]] = 0
    for j in range(where_clean[1],C):
        room[R][j] = room[R][j+1]
        room[R][j+1] = 0
    for i in range(R,where_clean[0]+1,-1):
        room[i][C] = room[i-1][C]
        room[i-1][8] = 0
    for j in range(C,where_clean[1]+1,-1):
        room[where_clean[0]+1][j] = room[where_clean[0]+1][j-1]
        room[where_clean[0]+1][j-1] = 0

mise_sum = 0
for i in range(1,R+1):
    for j in range(1,C+1):
        if room[i][j] > 0:
            mise_sum += room[i][j]
print(mise_sum)