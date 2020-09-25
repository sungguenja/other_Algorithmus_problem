def solution(flowers):
    answer = 0
    flowers.sort(key=lambda x: x[0])
    flw = {}
    for i in range(len(flowers)):
        for j in range(flowers[i][0],flowers[i][1]):
            flw[j] = 1
    answer = len(flw.keys())
    return answer

print(solution([[3,4],[4,5],[6,7],[8,10]]))