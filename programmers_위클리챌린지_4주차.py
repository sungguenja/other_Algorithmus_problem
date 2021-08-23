def returnTableList(table):
    result = []
    field_list = []
    for i in range(len(table)):
        lang_list = list(table[i].split())
        score_dict = {}
        for j in range(1,len(lang_list)):
            score_dict[lang_list[j]] = 5-j+1
        result.append(score_dict)
        field_list.append(lang_list[0])
    return result,field_list

def solution(table, languages, preference):
    score_table,field_list = returnTableList(table)
    point = [0]*len(table)
    for i in range(len(languages)):
        now_languages = languages[i]
        additional_point = preference[i]
        for j in range(len(table)):
            if score_table[j].get(now_languages) != None:
                point[j] += additional_point*score_table[j][now_languages]
    
    answer_point = -1
    answer = ''
    for i in range(len(field_list)):
        if point[i] > answer_point:
            answer_point = point[i]
            answer = field_list[i]
        elif point[i] == answer_point:
            check_list = [answer,field_list[i]]
            check_list.sort()
            answer = check_list[0]
    return answer