def solution(s):
    if len(s) != 0:
        answer = ''
        case = [0]*2500*2499
        cnt = -1
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    cnt+=1
                    case[cnt] = [i,j]
        for ca in case:
            if len(answer) == len(s):
                break
            if ca == 0:
                break
            if ca[1]-ca[0]+1<=len(answer):
                continue
            now = s[ca[0]:ca[1]+1]
            for k in range(len(now)//2+1):
                if now[k] != now[-1*k-1]:
                    break
            else:
                if len(answer)<len(now):
                    answer = now
        if answer == '':
            answer = 'a'
    else:
        answer = ''
    return len(answer)

print(solution("abcdcba"))
print(solution("abacde"))
print(solution('abccba'))
print(solution('aaaaaa'))
print(solution('aaaaaaa'))
print(solution('a'))