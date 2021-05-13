from abc import ABCMeta


def findDivisor(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt += 1
    
    if cnt%2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if findDivisor(i):
            answer += i
        else:
            answer -= i
    return answer