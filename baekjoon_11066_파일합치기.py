import sys
N = int(input())
for t in range(N):
    K = int(input())
    file_list = list(map(int,input().split()))
    consume = {-1:0} # 0번부터 i번까지

    for i in range(K):
        consume[i] = consume[i-1] + file_list[i]

    dp = [[0]*K for i in range(K)]

    for length in range(1,K):
        for start in range(K):
            end = start + length
            if end >= K:
                break
            dp[start][end] = sys.maxsize
            for divide_point in range(start,end):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][divide_point] + dp[divide_point+1][end] + consume[end] - consume[start-1]
                )
    
    print(dp[0][K-1])