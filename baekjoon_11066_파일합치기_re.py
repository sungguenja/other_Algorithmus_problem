import sys
input = sys.stdin.readline
for t in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    dp = [[0]*N for i in range(N)]
    consume = {-1:0}
    for i in range(N):
        consume[i] = arr[i] + consume[i-1]
    
    for length in range(1,N):
        for start in range(N):
            end = start + length
            if end >= N:
                break
            dp[start][end] = sys.maxsize
            for divide_point in range(start,end):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][divide_point] + dp[divide_point+1][end] + consume[end] - consume[start - 1]
                )
    print(dp[0][N-1])