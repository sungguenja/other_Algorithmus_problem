import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

N = int(input())
dp = [[0,0] for i in range(N+1)]
visit = [False]*(N+1)
lines = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    lines[a].append(b)
    lines[b].append(a)

def dfs(now):
    visit[now] = True
    dp[now][0] = 1
    for goal in lines[now]:
        if not visit[goal]:
            dfs(goal)
            dp[now][0] += min(dp[goal])
            dp[now][1] += dp[goal][0]

dfs(1)
print(min(dp[1]))