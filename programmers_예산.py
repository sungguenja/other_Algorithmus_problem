def solution(budgets,M):
    answer = 0
    save_sum = 0
    if sum(budgets) == M:
        answer = max(budgets)
    else:
        left = 0
        right = max(budgets)
        while left<=right:
            middle = (left+right)//2
            for_sum = 0
            for i in budgets:
                if i<=middle:
                    for_sum+=i
                else:
                    for_sum+=middle
            if for_sum<=M:
                if for_sum>save_sum:
                    save_sum = for_sum
                    answer = middle
                left = middle+1
            else:
                right = middle-1
    return answer

print(solution([485, 485, 485, 485],485))