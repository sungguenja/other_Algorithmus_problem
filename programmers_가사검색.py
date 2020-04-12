def solution(words, queries):
    answer = [0]*len(queries)
    for i in range(len(queries)):
        trigger = False
        cnt = queries[i].count('?')
        quar = queries[i]
        q_len = len(quar)
        if cnt == q_len:
            trigger = True
        if trigger:
            for j in words:
                if cnt == len(j):
                    answer[i] += 1
        else:
            if quar[0] == '?':
                quar = quar.split('?')[-1]
                for j in words:
                    if len(j)==q_len and j.endswith(quar):
                        answer[i]+=1
            else:
                quar = quar.split('?')[0]
                for j in words:
                    if len(j)==q_len and j.startswith(quar):
                        answer[i]+=1

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))