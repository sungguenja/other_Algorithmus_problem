pin_list = list(map(int,input().split()))
answer = 0
i = 0
frame = len(pin_list)
answer_list = []
count = 0
trigger = False
while i < frame:
    before_answer = answer
    if trigger and count == 0:
        if pin_list[i] == 10:
            i += 1
        else:
            i += 2
        trigger = False
        continue
    if pin_list[i] == 10:
        count += 1
        answer += pin_list[i] + pin_list[i+1] + pin_list[i+2]
        i += 1
    elif i + 1 < frame and pin_list[i] + pin_list[i+1] == 10:
        
        count += 1
        answer += pin_list[i] + pin_list[i+1] + pin_list[i+2]
        i += 2
    else:
        
        count += 1
        answer += pin_list[i] + pin_list[i+1]
        i += 2
        
    if count == 10:
        count = 0
        trigger = True
        answer_list.append(answer)
        answer = 0
        
answer_list = list(map(str,answer_list))
print(" ".join(answer_list))