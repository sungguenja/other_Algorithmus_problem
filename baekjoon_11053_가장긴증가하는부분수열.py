N=int(input())

num_list = [0]
num_list.extend(list(map(int,input().split())))
num_rank = [0]*(len(num_list))

for i in range(1,N+1):
    z=0
    for j in range(i):
        if num_list[i]>num_list[j] and num_rank[j]>=z:
            z=num_rank[j]
    num_rank[j+1] = z+1
print(max(num_rank[N]))