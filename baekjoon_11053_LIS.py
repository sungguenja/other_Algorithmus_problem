N=int(input())

num_list = [0]
num_list.extend(list(map(int,input().split())))
num_rank = [0]*(N+1)

for i in range(1,N+1):
    z=0
    for j in range(i):
        if num_list[j]<num_list[i] and z<=num_rank[j]:
            z=num_rank[j]+1
    num_rank[j+1] = z
print(num_rank)