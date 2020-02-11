N,M = map(int, input().split())
chicken_map = []

for _ in range(N):                          # 치킨지도(치킨먹고싶다)
    horizon = []
    horizon = list(map(int, input().split()))
    chicken_map.append(horizon)

house = []                                  # 집 위치
chicken = []                                # 치킨 위치

for i in range(N):
    for j in range(N):
        if chicken_map[i][j] == 1:
            house.append([i,j])
        elif chicken_map[i][j] == 2:
            chicken.append([i,j])
