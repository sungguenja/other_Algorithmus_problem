def solution(food_times, k):
    answer = 0
    i = 0
    cnt = 1
    N = len(food_times)
    for t in range(k):
        if i == N:
            cnt += 1
            i = 0
        if food_times[i] >= cnt:
            i += 1
    answer = i
    return answer