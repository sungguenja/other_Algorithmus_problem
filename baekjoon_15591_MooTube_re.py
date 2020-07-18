def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

N,Q = map(int,input().split())
p = [0]*(N+1)
rank = [0]*(N+1)
usado = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    make_set(i)

for i in range(Q):
    start,end,point = map(int,input().split())
    usado[start][end] = point
    union(start,end)
print(usado)
print(p)
print(rank)