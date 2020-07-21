def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def solution(start,end,K_cost,cost=1000000001,whe=-1):
    global answer
    print(cost,start,end,whe)
    if end == whe:
        if K_cost<=cost:
            answer += 1
        return
    
    for i in range(len(p)):
        if visit[i] == 0:
            if p[i] == start:
                visit[i] = 1
                solution(i,end,K_cost,min(cost,usado[start][i]),i)
                visit[i] = 0
            elif p[start] == i:
                visit[start] = 1
                solution(i,end,K_cost,min(cost,usado[i][start]),i)
                visit[start] = 0

N,Q = map(int,input().split())
p = [i for i in range(N+1)]
rank = [0]*(N+1)
usado = [[0]*(N+1) for i in range(N+1)]

for i in range(N-1):
    start,end,point = map(int,input().split())
    usado[start][end] = point
    usado[end][start] = point
    p[start] = end

for i in range(Q):
    K,V = map(int,input().split())
    answer = 0
    visit = [0]*(N+1)
    solution(V,V,K)
    print(answer)