N,M = map(int,input().split())

friend = [[0]*N for _ in range(N)]

for _ in range(M):
    fre1,fre2 = map(int,input().split())
    friend[fre1-1][fre2-1] = 1
    friend[fre2-1][fre1-1] = 1

for i in range(N):
    visit = [[0]*N for _ in range(N)]
    for j in range(N):
        que = [[i,z] for z in range(N)]
        while que != 0:
            point = que.pop()
            start, end = point[0], point[1]
            if visit[start][end] == 0 and friend[start][end] == 1:
                visit[start][end] += friend[start][end]
                for k in range(N):
                    que.append([end,k])