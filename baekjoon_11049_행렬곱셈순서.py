import sys
N = int(input())
matrix = [0]*N
for i in range(N):
    matrix[i] = list(map(int,input().split()))
    
dp = [[0]*N for i in range(N)]

for length in range(1,N):
    for start in range(N-length):
        end = start + length
        if end >= N:
            break
        if length == 1:
            dp[start][end] = matrix[start][0]*matrix[start][1]*matrix[end][1]
            continue
        dp[start][end] = sys.maxsize
        for divide_point in range(start,end):
            dp[start][end] = min(
                dp[start][end],
                dp[start][divide_point] + dp[divide_point+1][end] + (matrix[start][0] * matrix[divide_point][1] * matrix[end][1])
            )

print(dp[0][N-1])