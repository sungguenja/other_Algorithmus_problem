def solution(enter, leave):
    answer = [[] for _ in range(len(enter)+1)]
    people_stack = []
    enter_position = 0
    leave_position = 0
    
    checker = [0]*(len(enter)+1)
    
    while enter_position < len(enter) and leave_position < len(enter):
        if checker[leave[leave_position]] == 1:
            people_stack.remove(leave[leave_position])
            leave_position += 1
        else:
            answer[enter[enter_position]] = people_stack[:]
            people_stack.append(enter[enter_position])
            checker[enter[enter_position]] = 1
            enter_position += 1
            
    for p, person in enumerate(answer):
        for met in person:
            answer[met].append(p)
    return [len(set(i)) for i in answer][1:]