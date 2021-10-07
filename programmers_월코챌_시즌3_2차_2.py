def solution(n, left, right):
    answer = [None]*(right-left+1)
    cnt = 0
    for i in range(left,right+1):
        quotient = i // n
        remainder = i % n
        if quotient > remainder:
            answer[cnt] = quotient+1
        else:
            answer[cnt] = remainder+1
        cnt += 1
    return answer