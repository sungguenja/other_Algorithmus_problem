N,K = map(int,input().split())
temp = list(map(int,input().split()))

max_sum = 0
for x in range(K):
    max_sum += temp[x]

for i in range(1,N-K):
    now_num = 0
    for x in range(K):
        now_num += temp[i+x]
    if max_sum < now_num:
        max_sum = now_num
print(max_sum)