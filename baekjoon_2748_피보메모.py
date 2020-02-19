def F(N):
    memo = [[1,0],[0,1]]

    if N==0:
        return ' '.join(map(str,memo[0]))
    elif N==1:
        return ' '.join(map(str,memo[1]))
    else:
        for i in range(2,N+1):
            memo.append([memo[i-1][0]+memo[i-2][0],memo[i-1][1]+memo[i-2][1]])
        return ' '.join(map(str,memo[N]))

for t in range(int(input())):
    print(F(int(input())))