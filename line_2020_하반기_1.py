def solution(boxes):
    answer = 0
    category = {}
    for i in range(len(boxes)):
        if category.get(boxes[i][0]) == None:
            category[boxes[i][0]] = 1
        else:
            category[boxes[i][0]] = 2
        if category.get(boxes[i][1]) == None:
            category[boxes[i][1]] = 1
        else:
            category[boxes[i][1]] = 2
    for i in category.values():
        if i == 1:
            answer += 1
    print(answer)
    return answer//2