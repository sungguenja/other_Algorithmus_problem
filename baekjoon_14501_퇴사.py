N=int(input())
schedule=[[0]*N for _ in range(N)]
for i in range(N):
    dead,money=map(int,input().split())
    if i+dead<N:
        for j in range(i,i+dead):
            schedule[i][j] = money
case = [[0]*N for _ in range(N)]
