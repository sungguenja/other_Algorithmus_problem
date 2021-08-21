from sys import stdin
input = stdin.readline

N,M,L,K = map(int,input().split())
sky = []
for i in range(K):
    x,y = map(int,input().split())
    sky.append((x,y))

answer = -1
def checkSky(x,y):
    count = 0
    for star in sky:
        if x<=star[0]<=x+L and y<=star[1]<=y+L:
            count += 1
    return count

for star_1 in sky:
    for star_2 in sky:
        answer = max(answer,checkSky(star_1[0],star_2[1]))

print(K-answer)