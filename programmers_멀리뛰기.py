from math import factorial
def solution(n):
    answer = 0
    a = n
    b = 0
    while a>=0:
        answer += factorial(a+b)//(factorial(a)*factorial(b))
        a-=2
        b+=1
    return answer
    

for i in range(1,25):
    print(solution(i))