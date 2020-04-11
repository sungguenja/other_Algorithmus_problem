def solution(p):
    if p == '':
        return p
    else:
        stack = []
        for i in range(len(p)):
            if p[i] == '(':
                stack.append('(')
            elif p[i] == ')':
                if stack == []:
                    trigger = False
                    break
                else:
                    stack.pop()
        else:
            trigger = True
        if trigger:
            return p
        else:
            cnt = 0
            for i in range(len(p)):
                if p[i] == '(':
                    cnt += 1
                elif p[i] == ')':
                    cnt -=1
                if cnt == 0:
                    break
            u = p[:i+1]
            v = p[i+1:]
            print(u,v)
            stack = []
            for i in range(len(u)):
                if u[i] == '(':
                    stack.append('(')
                elif u[i] == ')':
                    if stack == []:
                        trigger = False
                        break
                    else:
                        stack.pop()
            else:
                trigger = True
            if trigger:
                return u + solution(v)
            else:
                now_v = '(' + solution(v) + ')'
                for i in range(1,len(u)-1):
                    if u[i] == '(':
                        now_v += ')'
                    elif u[i] == ')':
                        now_v += '('
                return now_v

answer = ''
print(3,solution("(()())()"))
answer = ''
print(3,solution('()'))
answer = ''
print(3,solution("()))((()"))