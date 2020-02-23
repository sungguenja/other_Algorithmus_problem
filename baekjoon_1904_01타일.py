def tile(N):
    dp = [0,1,2]
    if N<len(dp):
        return dp[N]
    else:
        for i in range(3,N+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[N]

print(tile(int(input())))