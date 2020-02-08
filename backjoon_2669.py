coordinate = [[0]*100 for _ in range(100)]
for _ in range(4):
    X1,Y1,X2,Y2 = map(int, input().split())
    for i in range(Y1,Y2):
        for j in range(X1,X2):
            coordinate[i][j] += 1

area = 0
for i in range(100):
    for j in range(100):
        if coordinate[i][j] > 0:
            area += 1

print(area)