N,M=map(int,input().split())
num_list = list(map(int,input().split()))

left = 0
right = 0
cnt = 0
now = num_list[0]
while right < N and left < N:
    if now < M:
        right += 1
        if right >= N:
            break
        now += num_list[right]
    else:
        if now == M:
            cnt += 1
        now -= num_list[left]
        left += 1
print(cnt)