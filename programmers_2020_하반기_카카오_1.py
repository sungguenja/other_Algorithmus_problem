def solution(new_id):
    answer = ''
    # 1단계
    answer = new_id.lower()
    can_case = [chr(i) for i in range(97,123)]
    can_case += ['0','1','2','3','4','5','6','7','8','9','-','_','.']
    answer_re = ''
    # 2던걔
    for i in range(len(answer)):
        if answer[i] in can_case:
            answer_re += answer[i]
    answer = answer_re
    answer_re = ''
    # 3단계
    for i in range(len(answer)):
        if i==0:
            answer_re += answer[i]
            continue
        if answer_re[-1] == '.' and answer[i] == '.':
            continue
        answer_re += answer[i]
    # 4-1단계
    if answer_re[0] == '.':
        answer = answer_re[1:]
    else:
        answer = answer_re
    # 4-2단계
    if len(answer)>=1 and answer[-1] == '.':
        answer = answer[:-1]
    answer_re = ''
    # 5단계
    for i in range(len(answer)):
        if answer[i] == ' ':
            answer_re += 'a'
        else:
            answer_re += answer[i]
    # 6단계
    if len(answer_re) >= 16:
        answer = answer_re[:15]
    else:
        answer = answer_re
    # 4-2단계
    if len(answer)>=1 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if answer == '':
        answer = 'a'
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))