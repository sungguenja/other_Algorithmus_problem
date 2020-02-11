di = 1
dj = 1
N,M = map(int,input().split())
i,j = map(int,input().split())
for t in range(int(input())):
    i += di
    j += dj
    if i == N or i == 0:
        di *= -1
    if j == M or j == 0:
        dj *= -1
print(i,j)