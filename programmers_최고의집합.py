def solution(n, s):
    answer = []
    if n>s:
        answer = [-1]
    elif n==s:
        answer = [1]*n
    else:
        share = s//n
        remainder = s%n
        answer = [share]*n
        for i in range(remainder):
            answer[i] += 1
        answer.sort()
    return answer