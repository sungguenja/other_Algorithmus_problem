N = int(input())
num_list = list(map(int,input().split()))
X = int(input())
cnt = 0
num_list.sort()
left = 0
right = N-1
while left<right and right<N:
    now = num_list[left]+num_list[right]
    if now < X:
        left += 1
    elif now > X:
        right -= 1
    else:
        cnt += 1
        right -= 1
        left += 1
print(cnt)