def firstStep(new_id):
    answer = ''
    for i in new_id:
        answer += i.lower()
    return secondStep(answer)

def secondStep(new_id):
    answer = ''
    can = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.','1','2','3','4','5','6','7','8','9','0']
    for i in new_id:
        if i in can:
            answer += i
    return thirdStep(answer)

def thirdStep(new_id):
    answer = ''
    trigger = True
    for i in new_id:
        if i != '.':
            trigger = True
            answer += i
        else:
            if trigger:
                answer += i
                trigger = False
    return fourthStep(answer)

def fourthStep(new_id):
    answer = new_id
    if len(answer) >= 1 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == '.':
        answer = answer[:-1]
    return fifthStep(answer)

def fifthStep(new_id):
    answer = new_id
    if answer == '':
        answer = 'a'
    return sixthStep(answer)

def sixthStep(new_id):
    answer = new_id
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    return seventhStep(answer)

def seventhStep(new_id):
    answer = new_id
    while len(answer) < 3:
        answer += answer[-1]
    return answer

def solution(new_id):
    answer = firstStep(new_id)
    return answer