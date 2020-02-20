import sys

INF = sys.maxsize
V,E=map(int,input().split())
start = int(input())
node = [['INF']*V for _ in range(V)]

for _ in range(E):
    S,E,P=map(int,input().split())
    node[S-1][E-1] = P

que = [[0,0]]
dis_node = [[0]*V for _ in range(V)]
que = [[0,0,[0,0,0,0,0]]]

while que != []:
    X = que.pop()
    start,dis,visit = X[0],X[1],X[2][:]
    for j in range(V):
        if visit[j] == 0 and node[start][j] != 'INF':
            visit[j]=1
            dis_node[start][j] = dis + node[start][j]
            que.append([j,dis_node[start][j],visit])
