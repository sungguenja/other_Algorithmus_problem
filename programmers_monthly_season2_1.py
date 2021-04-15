def solution(absolutes, signs):
    answer = 0
    N = len(absolutes)
    for i in range(N):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer