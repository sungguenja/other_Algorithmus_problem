def solution(info, query):
    info = [list(i.split()) for i in info]
    query = [list(i.split()) for i in query]
    answer = [0]*len(query)
    for i in range(len(info)):
        for j in range(len(query)):
            if (query[j][0]=='-' or info[i][0]==query[j][0]) and (query[j][2]=='-' or info[i][1] == query[j][2]) and (query[j][4]=='-' or info[i][2]==query[j][4]) and (query[j][6]=='-' or info[i][3]==query[j][6]) and (query[j][7]=='-' or int(info[i][4])>=int(query[j][7])):
                answer[j]+=1
    return answer