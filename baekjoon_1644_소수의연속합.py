# pypy는 통과하는데....
def is_primary_num(num):
    rounded_num = round(num**(1/2)) + 1
    for i in range(2,rounded_num):
        if num%i == 0:
            return False
    return True

N = int(input())

prime_list = [0]*(N+3)

if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    left = 2
    right = 2
    now_sum = 0
    answer = 0

    if is_primary_num(N):
        prime_list[N] = 1
        answer = 1

    while left <= N and right <= N:
        if now_sum >= N:
            if now_sum == N:
                answer += 1
            
            now_sum -= left
            while left <= N:
                left += 1
                if prime_list[left] == 1:
                    break
        else:
            now_sum += right
            while right <= N:
                right += 1
                if prime_list[right] == 1 or is_primary_num(right):
                    prime_list[right] = 1
                    break
                
    print(answer)