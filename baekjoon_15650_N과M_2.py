def permunate(num_list,m,line=[]):

    if len(line) == m:
        line.sort()
        if line not in perm:
            perm.append(line)
            return

    for i in range(len(num_list)):
        if visit[i] == 0:
            visit[i] = 1
            permunate(num_list,m,line+[num_list[i]])
            visit[i] = 0

N,M=map(int,input().split())
N_list = list(range(1,N+1))
visit = [0]*N
perm = []
permunate(N_list,M)
for k in perm:
    print(' '.join(map(str,k)))