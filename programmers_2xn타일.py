def solution(n):
    answer = 2
    b_answer = 1
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for _ in range(2,n):
            answer, b_answer = answer+b_answer, answer
    return answer%1000000007