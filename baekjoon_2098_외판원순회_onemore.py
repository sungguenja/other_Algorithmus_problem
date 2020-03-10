import sys

def root(start,N,visit=1):
    if visit == (1<<N)-1:           # 끝을 내러 왔소
        if road[start][0] == INF:
            return INF
        else:
            return road[start][0]
    
    if DP[start][visit] != None:    # 이 경로를 지나서 돈을 낸 적이 있는가
        return DP[start][visit]

    cost = INF
    for i in range(N):
        if visit & (1<<i) == 0 and road[start][i] != 0:
            cost = min(cost,root(i,N,visit|(1<<i))+road[start][i])
    DP[start][visit] = cost
    return cost

N=int(input())
road=[list(map(int,input().split())) for _ in range(N)]
INF = sys.maxsize
DP = [[None]*(1<<N) for _ in range(N)]
for i in range(N):
    print(root(i,N,1<<i))
ans = INF
for k in DP:
    print(k)
print(ans)