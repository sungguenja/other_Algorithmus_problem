import sys

def dijkstra(K,V,node):
    INF = sys.maxsize

    S=[False]*V             # 방문 여부

    d=[INF]*V           # 거리 저장용
    d[K-1] = 0          # 자기 자신에게 가는 비용은 0이다.

    while True:
        m=INF
        N=-1

        for v in range(V):
            if not S[v] and m>d[v]:
                m=d[v]
                N=v

        if m==INF:
            break

        S[N] = True

        for v in range(V):
            if S[v]:
                continue
            else:
                distence = d[N] + node[N][v]
                if d[v] > distence:
                    d[v] = distence
    
    return d

INF = sys.maxsize
V,E=map(int,input().split())
start = int(input())
node = [[INF]*V for _ in range(V)]
for _ in range(E):
    S,E,P=map(int,input().split())
    node[S-1][E-1] = P

for d in dijkstra(start,V,node):
    print(d if d!=INF else 'INF')