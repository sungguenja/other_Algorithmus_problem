def solution(msg):
    answer = []
    msg_dic = {}
    last = 27
    now = 0
    N = len(msg)
    while now < N:
        if msg[now] not in msg_dic.keys():
            answer.append(ord(msg[now])-64)
            msg_dic[msg[now]] = ord(msg[now])-64
            msg_dic[msg[now:now+2]] = last
            last += 1
            now += 1
        else:
            end = now + 1
            while msg[now:end] in msg_dic.keys() and end <= N:
                end += 1
            if msg[now:end] not in msg_dic.keys():
                msg_dic[msg[now:end]] = last
                last += 1
            answer.append(msg_dic[msg[now:end-1]])
            now = end-1
    return answer

print(solution("ABABABABABABABAB"))