N,S = map(int,input().split())
num_list = list(map(int,input().split()))
left = 0
right = 0
now_sum = 0
answer = (N+1)**2
while left<=N and right<=N:
    if now_sum >= S:
        if answer > right-left:
            answer = right - left
        if left == N:
            break
        now_sum -= num_list[left]
        left += 1
    else:
        if right == N:
            break
        now_sum += num_list[right]
        right += 1
if answer == (N+1)**2:
    answer = 0
print(answer)