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

chicken_choice = [0]*len(chicken)           # 치킨 선택된 횟수

short = 0
for home in house:
    short_distance = N*2
    distance = 0
    for i in range(len(chicken)):
        if short_distance>abs(home[0]-chicken[i][0])+abs(home[1]-chicken[i][1]):
            short_distance = abs(home[0]-chicken[i][0])+abs(home[1]-chicken[i][1])
            z=i
            