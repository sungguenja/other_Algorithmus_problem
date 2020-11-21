def solution(s):
    check = {}
    for i in range(1,len(s)-1):
        if s[i] == '{':
            now = ''
        elif s[i] == '}':
            if check.get(now) == None:
                check[now] = 1
            else:
                check[now] += 1
            now = ''
        elif s[i] == ',':
            if now == '':
                continue
            if check.get(now) == None:
                check[now] = 1
            else:
                check[now] += 1
            now = ''
        else:
            now += s[i]
    answer = list(map(int,sorted(check,key=check.get,reverse=True)))
    return answer