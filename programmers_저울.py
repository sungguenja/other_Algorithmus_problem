def solution(weight):
    answer = sum(weight)+1
    if 1 in weight:
        for i in range(sum(weight)-1,1,-1):
            if i in weight:
                continue
            else:
                pass
    else:
        answer = 1
    return answer

print(solution([3, 1, 6, 2, 7, 30, 1]))