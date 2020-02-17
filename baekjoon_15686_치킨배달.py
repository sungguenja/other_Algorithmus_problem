N,M = map(int, input().split())
chicken_map = []


house = []                                  # 집 위치
chicken = []                                # 치킨 위치

for i in range(N):                          # 치킨지도(치킨먹고싶다)
    horizon = []
    horizon = list(map(int, input().split()))
    chicken_map.append(horizon)
    for j in range(N):
        if horizon[j] == 1:
            house.append([i,j])
        elif horizon[j] == 2:
            chicken.append([i,j])

chicken_case = []                           # 치킨 경우의 수
for i in range(1<<len(chicken)):
    ch_bi = list(bin(i)[2:])
    if ch_bi.count('1') != M:
        continue
    else:
        ch_ck = []
        for j in range(len(chicken)):
            if i&1<<j:
                ch_ck.append(chicken[j])
        chicken_case.append(ch_ck)

min_distance = (N**2)*N                    # 최소 치킨 거리

for i in range(len(chicken_case)):
    su = 0
    for j in range(len(house)):
        ch_dis = N**2
        for k in range(M):
            if ch_dis > abs(house[j][0]-chicken_case[i][k][0]) + abs(house[j][1]-chicken_case[i][k][1]):
                ch_dis = abs(house[j][0]-chicken_case[i][k][0]) + abs(house[j][1]-chicken_case[i][k][1])
        su += ch_dis
    if su < min_distance:
        min_distance = su
print(min_distance)