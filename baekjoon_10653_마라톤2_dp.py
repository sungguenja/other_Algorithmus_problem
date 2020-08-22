N,K = map(int,input().split())
checkpoint = [list(map(int,input().split())) for _ in range(N)]
jump = [[1,0],[2,1]]
cost = [[0]*(K+1) for _ in range(N)]
for i in range(N):
    for j in range(K+1):
        l = i+1 # 다음 위치 부터 점프를 계속 시키는것
        while l<N and j+l-i-1<=K:
            nj = j+l-i-1
            ni = l
            if cost[ni][nj] == 0:
                cost[ni][nj] = cost[i][j]+abs(checkpoint[ni][0]-checkpoint[i][0])+abs(checkpoint[ni][1]-checkpoint[i][1])
            else:
                cost[ni][nj] = min(cost[ni][nj],cost[i][j]+abs(checkpoint[ni][0]-checkpoint[i][0])+abs(checkpoint[ni][1]-checkpoint[i][1]))
            l+=1
print(cost[-1][-1])