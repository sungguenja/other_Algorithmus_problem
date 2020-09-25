def solution(histogram):
    answer = 0
    for i in range(len(histogram)-2):
        for j in range(i+2,len(histogram)):
            vertical = min(histogram[i],histogram[j])
            horizontal = j-i-1
            answer = max(answer,vertical*horizontal)
    return answer