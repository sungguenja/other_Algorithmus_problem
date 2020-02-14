def permunate(num_list,m,line=[]):

    if len(line) == m:
        perm.append(line)
        return

    for i in range(len(num_list)):
        permunate(num_list,m,line+[str(num_list[i])])

N,M=map(int,input().split())
N_list = list(range(1,N+1))
perm = []
permunate(N_list,M)
for k in perm:
    print(' '.join(k))