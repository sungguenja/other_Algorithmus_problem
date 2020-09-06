direction = [[0,1],[1,0],[0,-1],[-1,0]]
def after(X):
    return X-1
N,M = map(int,input().split())
room = [[0]*N for i in range(N)]
switch = [list(map(after,(map(int,input().split())))) for i in range(M)]

cnt = 0
for i in range(N):
    for j in range(N):
        if room[i][j]==1:
            cnt+=1
print(cnt)