from math import factorial
def solution(n, k):
    answer = []
    save_k = k-1
    num_list = list(range(1,n+1))
    for _ in range(n):
        for i in range(n):
            if i*factorial(n-len(answer)-1)<= save_k < (i+1)*factorial(n-len(answer)-1):
                save_k -= i*factorial(n-len(answer)-1)
                answer.append(num_list.pop(i))
                break
    return answer

print(solution(3,5))
print(solution(4,5))
print(solution(4,4))
print(solution(4,7))