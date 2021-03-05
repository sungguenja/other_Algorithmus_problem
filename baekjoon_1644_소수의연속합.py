def is_primary_num(num):
    rounded_num = round(num**(1/2)) + 1
    for i in range(2,rounded_num):
        if num%i == 0:
            return False
    return True

N = int(input())
if N == 1 or N == 2:
    print(1)
else:
    left = 2
    right = 2
    now_sum = 0
    answer = 0
    
    while left <= N and right <= N:
        print(left,right,now_sum)
        if now_sum >= N:
            if now_sum == N:
                answer += 1
            
            now_sum -= left
            while left <= N:
                left += 1
                if is_primary_num(left):
                    break
        else:
            now_sum += right
            while right <= N:
                right += 1
                if is_primary_num(right):
                    break
                
    print(answer)