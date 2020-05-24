def solution(genres, plays):
    answer = []
    answer_dict = dict()
    for i in range(len(plays)):
        if answer_dict.get(genres[i]) == None:
            answer_dict[genres[i]] = [plays[i],[i]]
        else:
            answer_dict[genres[i]][0] += plays[i]
            answer_dict[genres[i]][1].append(i)
    N = len(answer_dict)
    for _ in range(N):
        max_key = 0
        max_value = 0
        for key, value in answer_dict.items():
            if max_value<value[0]:
                max_key = key
                max_value = value[0]
        if len(answer_dict[max_key][1])>=2:
            for i in range(2):
                maximum = 0
                maximum_whe = 0
                maximum_whe_in = 0
                for j in range(len(answer_dict[max_key][1])):
                    if plays[answer_dict[max_key][1][j]]>maximum:
                        maximum = plays[answer_dict[max_key][1][j]]
                        maximum_whe = answer_dict[max_key][1][j]
                        maximum_whe_in = j
                answer.append(maximum_whe)
                answer_dict[max_key][1].pop(maximum_whe_in)
            del answer_dict[max_key]
        else:
            for i in range(1):
                maximum = 0
                maximum_whe = 0
                maximum_whe_in = 0
                for j in range(len(answer_dict[max_key][1])):
                    if plays[answer_dict[max_key][1][j]]>maximum:
                        maximum = plays[answer_dict[max_key][1][j]]
                        maximum_whe = answer_dict[max_key][1][j]
                        maximum_whe_in = j
                answer.append(maximum_whe)
                answer_dict[max_key][1].pop(maximum_whe_in)
            del answer_dict[max_key]
    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]))