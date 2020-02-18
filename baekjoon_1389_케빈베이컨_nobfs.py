su_len=999
def kevin(start,end,fre_len=0):
    global su_len
    
    if su_len<fre_len:
        return

    if start == end and su_len>fre_len:
        su_len = fre_len
        return

    for z in range(1,N+1):
        if visit[z] == 0 and friend[start][z] == 1:
            visit[z] = 1
            kevin(z,end,fre_len+1) == 1
            visit[z] = 0

N,M = map(int,input().split())

friend = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    fre1, fre2 = map(int,input().split())
    friend[fre1][fre2] = 1
    friend[fre2][fre1] = 1

min_len = N*M
V=N+5
for i in range(1,N+1):
    su = 0
    for j in range(1,N+1):
        if i==j:
            continue
        visit=[0]*(N+1)
        su_len = N*M
        kevin(i,j)
        su += su_len
    else:
        if min_len > su:
            min_len = su
            V=i
        elif min_len == su and V>i:
            V=i
print(V)