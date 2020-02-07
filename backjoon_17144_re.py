R, C, T = map(int, input().split())
room = [['B']*(C+2)]
for _ in range(R):                  #방만들기
    garo = []
    garo = ['B']+list(map(int, input().split()))+['B']
    room.append(garo)
room.append(['B']*(C+2))

dk = [[0,1],[1,0],[0,-1],[-1,0]]    # 4방향 확인용
where_clean=[]
for i in range(R):                  # 공기청정기 어디있냐
    if len(where_clean) == 2:
        break
    for j in range(C):
        if room[i][j] == -1:
            where_clean.append([i,j])
        if len(where_clean) == 2:
            break


for _ in range(T):                  # 횟수만 하면 되니까 _으로
    dust = []
    for t in range(R+2):              # 먼지 확산 저장용
        dust_garo=[]
        dust_garo=[0]*(C+2)
        dust.append(dust_garo)
    
    for i in range(1,R+1):              # 먼지 확산 조사
        for j in range(1,C+1):
            if room[i][j] > 0:
                cnt = 0
                for k in dk:
                    if room[i+k[0]][j+k[1]] == -1 or room[i+k[0]][j+k[1]] == 'B':
                        continue
                    else:
                        dust[i+k[0]][j+k[1]] += room[i][j]//5
                        cnt += 1
                room[i][j] -= (room[i][j]//5)*cnt

    for i in range(1,R+1):              # 미세먼지 확신시키기
        for j in range(1,C+1):
            room[i][j] += dust[i][j]
    
    for i in range(where_clean[0][0]-1,1,-1): # 공기청정기 윗쪽 실행
        room[i][where_clean[0][1]] = room[i-1][where_clean[0][1]]
    for j in range(where_clean[0][1],C):
        room[1][j] = room[1][j+1]
    for i in range(1,where_clean[0][0]):
        room[i][C] = room[i+1][C]
    for j in range(C,where_clean[0][1]+1,-1):
        room[where_clean[0][0]][j] = room[where_clean[0][0]][j-1]
    room[where_clean[0][0]][where_clean[0][1]+1] = 0
    
    for i in range(where_clean[1][0]+1,R): # 공기청정기 아래쪽 실행
        room[i][where_clean[1][1]] = room[i+1][where_clean[1][1]]
    for j in range(where_clean[1][1],C):
        room[R][j] = room[R][j+1]
    for i in range(R,where_clean[1][0],-1):
        room[i][C] = room[i-1][C]
    for j in range(C,where_clean[1][1]+1,-1):
        room[where_clean[1][0]][j] = room[where_clean[1][0]][j-1]
    room[where_clean[1][0]][where_clean[1][1]+1] = 0

dust_sum = 0
for i in range(1,R+1):                  # 미세먼지 합                  
    for j in range(1,C+1):              # 끝난 결과이니 for문 밖에서 해야함
        if room[i][j] > 0:          # -1은 공기청정기라 0초과로 해줘야함
            dust_sum += room[i][j]
    
print(dust_sum)