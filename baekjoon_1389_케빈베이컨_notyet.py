su_len=999
def kevin(start,end,fre_len=0):
    global su_len
    
    if start == end and su_len>fre_len:
        su_len = fre_len
        return 

    for z in range(N):
        if visit[z] == 0:
            visit[z] = 1
            kevin(z,end,fre_len+1)
            visit[z] = 0

N,M = map(int,input().split())

friend = [[0]*N for _ in range(N)]

for _ in range(M):
    fre1, fre2 = map(int,input().split())
    friend[fre1-1][fre2-1] = 1
    friend[fre2-1][fre1-1] = 1

min_len = N*M
for i in range(N):
    su = 0
    for j in range(N):
        if i==j:
            continue
        visit=[0]*N
        su_len = N*M
        kevin(i,j)
        su += su_len
    if min_len>su:
        min_len=su
        V=i
    elif min_len == su:
        if V>i:
            V=i
    print(su,i)
    print()
print(V)