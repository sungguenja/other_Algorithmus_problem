INF = 300000*20000

def dijkstra(V,node,start):
    global INF

    D = [INF]*V
    P = [None]*V
    visit = [False]*V
    D[start] = 0

    for _ in range(V):
        min_num=INF
        minindex=-1
        for i in range(V):
            if not visit[i] and D[i]<min_num:
                min_num=D[i]
                minindex=i
        visit[minindex] = True
        for i in range(V):
            if not visit[i] and D[minindex]+node[minindex][i]<D[i]:
                D[i] = D[minindex]+node[minindex][i]
                P[i] = minindex

    return D

K,V=map(int,input().split())
start = int(input())
root = [[INF]*K for _ in range(K)]
for _ in range(V):
    i,j,w=map(int,input().split())
    root[i-1][j-1] = w

now = dijkstra(K,root,start-1)
for i in range(K):
    if now[i] == INF:
        print('INF')
    else:
        print(now[i])