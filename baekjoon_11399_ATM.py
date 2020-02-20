M=int(input())
time = list(map(int,input().split()))
time.sort()
tome_sum = 0
for i in range(M):
    tome_sum += sum(time[:i+1])
print(tome_sum)
