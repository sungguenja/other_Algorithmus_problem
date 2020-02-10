N,K=map(int,input().split())
temp = list(map(int, input().split()))

max_sum = sum(temp[:K])
for i in range(1,N-K):
    if max_sum<sum(temp[i:i+K]):
        max_sum = sum(temp[i:i+K])
print(max_sum)