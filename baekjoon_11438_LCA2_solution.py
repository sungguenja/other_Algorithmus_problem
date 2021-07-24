import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
LENGTH = 21

N = int(input())
parent = [[0]*LENGTH for i in range(N+1)]
visit = [False]*(N+1)
depth = [0]*(N+1)
route = [[] for i in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    route[a].append(b)
    route[b].append(a)

def checkDepthWithDFS(x,status):
    visit[x] = True
    depth[x] = status

    for node in route[x]:
        if visit[node]:
            continue
        parent[node][0] = x
        checkDepthWithDFS(node,status+1)

def setParent():
    checkDepthWithDFS(1,0)
    for i in range(1,LENGTH):
        for j in range(1,N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def LCA(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    
    for i in range(LENGTH-1,-1,-1):
        if depth[b] - depth[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a
    
    for i in range(LENGTH-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[a][0]

setParent()

M = int(input())

for i in range(M):
    a,b = map(int,input().split())
    print(LCA(a,b))