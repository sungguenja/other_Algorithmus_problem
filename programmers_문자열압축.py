def solution(s):
    answer = ''
    for i in range(1,len(s)//2+1):
        now_ans = ''
        j=0
        while j<len(s):
            cnt=1
            X=s[j:j+i]
            while s[j:j+i] == s[j+i:j+2*i]:
                cnt+=1
                j=j+i
            if cnt>1:
                now_ans += str(cnt)
            now_ans += X
            j+=i
        if answer == '' or len(answer) > len(now_ans):
            answer = now_ans
    if answer == '':
        answer = s
    return len(answer)

print(solution('aabbaccc'))
print(solution("ababcdcdababcdcd"))