M,N = map(int,input().split())

bracket = [list(map(int,input().split())) for _ in range(N)]

direction = [[0,1],[1,0],[0,-1],[-1,0]]
day = 0
stack=[]
for i in range(N):
    for j in range(M):
        if bracket[i][j] == 1:
            stack.append([i,j])

while stack != []:
    X=stack.pop(0)
    ni,nj=X[0],X[1]
    for k in direction:
        if 0<=ni+k[0]<N and 0<=nj+k[1]<M:
            if bracket[ni+k[0]][nj+k[1]] == 0:
                stack.append([ni+k[0],nj+k[1]])
                bracket[ni+k[0]][nj+k[1]] = bracket[ni][nj] + 1


for i in bracket:
    if day < max(i):
        day = max(i)
    if 0 in i:
        day = 0
        break
print(day-1)