def way(start,end,N,cost=0,visit=[]):
    global min_cost

    if cost>min_cost:
        return

    if len(visit)==N and start==end and cost<min_cost:
        min_cost=cost
        return
    
    for i in range(N):
        if i not in visit and road[start][i] != 0:
            way(i,end,N,cost+road[start][i],visit+[i])

N=int(input())
road = [list(map(int,input().split())) for _ in range(N)]
min_cost=0
for k in road:
    min_cost+=sum(k)

for i in range(N):
    way(i,i,N)
print(min_cost)