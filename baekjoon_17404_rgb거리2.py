import sys
input = sys.stdin.readline
answer = sys.maxsize

N = int(input())
cost = [list(map(int,input().split())) for i in range(N)]

for init_color in range(3):
    dp = [[0]*N for i in range(3)]

    for i in range(3):
        if i == init_color:
            dp[i][0] = cost[0][i]
            continue
        dp[i][0] = sys.maxsize

    for i in range(1,N):
        dp[0][i] = cost[i][0] + min(dp[1][i-1],dp[2][i-1])
        dp[1][i] = cost[i][1] + min(dp[0][i-1],dp[2][i-1])
        dp[2][i] = cost[i][2] + min(dp[0][i-1],dp[1][i-1])
    
    for i in range(3):
        if i != init_color:
            answer = min(answer,dp[i][-1])

print(answer)