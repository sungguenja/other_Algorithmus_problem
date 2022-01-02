import sys
input = sys.stdin.readline

N = int(input())
func = [0] + list(map(int,input().split()))
dp = [[func[i]] for i in range(N+1)]

for j in range(1,19):
    for i in range(1,N+1):
        dp[i].append(dp[dp[i][j-1]][j-1])

for _ in range(int(input())):
    cnt, start = map(int,input().split())
    for j in range(18,-1,-1):
        if cnt >= 1 << j:
            cnt -= 1 << j
            start = dp[start][j]

    print(start)