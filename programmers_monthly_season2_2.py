def solution(s):
    answer = 0
    N = len(s)
    opened = ['(','[','{']
    closed = [')',']','}']
    for i in range(N):
        stack = []
        for j in range(i,i+N):
            if s[j%N] in opened:
                stack.append(s[j%N])
            else:
                if len(stack) == 0:
                    break
                now = stack.pop()
                if closed.index(s[j%N]) != opened.index(now):
                    break
        else:
            if len(stack) == 0:
                answer += 1
    return answer