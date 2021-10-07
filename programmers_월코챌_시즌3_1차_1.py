def solution(numbers):
    answer = 0
    check_list = [False]*10
    for num in numbers:
        check_list[num] = True
    
    for i in range(10):
        if not check_list[i]:
            answer += i
            
    return answer