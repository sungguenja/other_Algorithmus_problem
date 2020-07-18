di = [0,-1,0,1]
dj = [1,0,-1,0]
dragon = [[0]*110 for i in range(110)]
for _ in range(int(input())):
    x,y,d,g = map(int,input().split())
    dragon[y][x] += 1
    nj = x+dj[d]
    ni = y+di[d]
    dragon[ni][nj] += 1
    dragon_generation = [d]
    for i in range(g):
        now_generation = []
        for j in range(len(dragon_generation)-1,-1,-1):
            ni += di[(dragon_generation[j]+1)%4]
            nj += dj[(dragon_generation[j]+1)%4]
            dragon[ni][nj] += 1
            now_generation.append((dragon_generation[j]+1)%4)
        dragon_generation.extend(now_generation)

squre = 0
for i in range(108):
    for j in range(108):
        if dragon[i][j] >= 1 and dragon[i+1][j] >= 1 and dragon[i][j+1] >= 1 and dragon[i+1][j+1] >= 1:
            squre += 1
print(squre)