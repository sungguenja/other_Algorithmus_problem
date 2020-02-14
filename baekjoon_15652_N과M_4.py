def permunate(num_list,m,line=[]):

    if len(line) == m:
        perm.append(line)
        return

    for i in range(len(num_list)):
        if visit[i] != m:
            if line == []:
                visit[i] += 1
                permunate(num_list,m,line+[num_list[i]])
                visit[i] -= 1
            else:
                if line[-1]<=num_list[i]:
                    visit[i] += 1
                    permunate(num_list,m,line+[num_list[i]])
                    visit[i] -= 1

N,M=map(int,input().split())
N_list = list(range(1,N+1))
perm = []
visit = [0]*N
permunate(N_list,M)
for k in perm:
    print(' '.join(map(str,k)))