M,N = map(int,input().split())

stack=[]
bracket = []
zero_stack = 0
for i in range(N):
    horizon = []
    horizon = list(map(int,input().split()))
    bracket.append(horizon)
    if 1 in horizon:
        stack.append([i,horizon.index(1)])
    zero_stack += horizon.count(0)

direction = [[0,1],[1,0],[0,-1],[-1,0]]
day = 1

while stack != []:
    X=stack.pop(0)
    ni,nj=X[0],X[1]
    for k in direction:
        if 0<=ni+k[0]<N and 0<=nj+k[1]<M:
            if bracket[ni+k[0]][nj+k[1]] == 0:
                stack.append([ni+k[0],nj+k[1]])
                bracket[ni+k[0]][nj+k[1]] = bracket[ni][nj] + 1
                if bracket[ni+k[0]][nj+k[1]]>day:
                    day = bracket[ni+k[0]][nj+k[1]]
                zero_stack -= 1
        if zero_stack == 0:
            break
    if zero_stack == 0:
        break

if zero_stack != 0:
    day = 0
print(day-1)