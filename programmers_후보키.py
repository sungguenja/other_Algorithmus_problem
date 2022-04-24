from itertools import combinations
def solution(relation):
    person_count = len(relation)
    properties_count = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, properties_count+1):
        combi.extend(combinations(range(properties_count), i))

    answer = []
    for combination_situation in combi:
        possible_list = [tuple(person[now_situation] for now_situation in combination_situation) for person in relation]
        
        if len(set(possible_list)) == person_count:
            for already_situation in answer:
                if set(already_situation).issubset(set(combination_situation)):
                    break
            else:
                answer.append(combination_situation)
    return len(answer)