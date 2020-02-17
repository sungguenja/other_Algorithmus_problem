M,N = map(int,input().split())

stack=[0]*N*M
bracket = [0]*N
zero_stack = 0
visit_bracket = [[N*M+1]*M for _ in range(N)]
num = 0
for i in range(N):
    horizon = []
    horizon = list(map(int,input().split()))
    bracket[i]=horizon
    for j in range(M):
        if horizon[j] == 1:
            stack[num]=[i,j]
            visit_bracket[i][j] = 1
            num += 1
        elif horizon[j] == 0:
            zero_stack += 1

direction = [[0,1],[1,0],[0,-1],[-1,0]]
day = 1
Z=0
while num != Z:
    X=stack[Z]
    ni,nj=X[0],X[1]
    Z += 1
    for k in direction:
        if 0<=ni+k[0]<N and 0<=nj+k[1]<M:
            if bracket[ni+k[0]][nj+k[1]] == 0 and visit_bracket[ni][nj]+1< visit_bracket[ni+k[0]][nj+k[1]]:
                stack[num]=[ni+k[0],nj+k[1]]
                visit_bracket[ni+k[0]][nj+k[1]] = visit_bracket[ni][nj] + 1
                num+=1
                if visit_bracket[ni+k[0]][nj+k[1]]>day:
                    day = visit_bracket[ni+k[0]][nj+k[1]]
                zero_stack -= 1
        if zero_stack == 0:
            break
    if zero_stack == 0:
        break

if zero_stack != 0:
    day = 0
print(day-1)