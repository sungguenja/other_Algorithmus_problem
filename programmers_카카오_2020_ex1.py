def solution(v):
    answer = []
    x_dict = dict()
    y_dict = dict()
    for i in range(len(v)):
        if x_dict.get(v[i][0]) == None:
            x_dict[v[i][0]] = 1
        else:
            x_dict[v[i][0]] += 1
        if y_dict.get(v[i][1]) == None:
            y_dict[v[i][1]] = 1
        else:
            y_dict[v[i][1]] += 1
    for key, value in x_dict.items():
        if value == 1:
            answer = [key]
            break
    for key, value in y_dict.items():
        if value == 1:
            answer.append(key)
            break
    return answer