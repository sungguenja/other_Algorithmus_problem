def solution(s):
    answer = []
    number_list = list(map(list,s))
    for num in range(len(number_list)):
        number = number_list[num]
        visit = [False]*len(number)
        i = 0
        for i in range(len(number)):
            if i+3<=len(number) and number[i] == '1' and number[i+1] == '1' and number[i+2] == '0':
                trigger = False
                for j in range(i):
                    if number[j:j+3] == ['1','1','1']:
                        trigger = True
                        break
                if trigger:
                    tmp = '110'
                    for k in range(3):
                        number[i+k] = '1'
                    for k in range(3):
                        number[j+k] = tmp[k]
                    i = j + 3
                else:
                    j = i + 3
                    while j < len(number) and number[j] == '1':
                        j += 1
                    if j == len(number):
                        break
                    tmp = []
                    while j < len(number):
                        tmp.append(number.pop())
                    while tmp:
                        number.insert(i,tmp.pop())
                        i += 1
                    for k in range(3):
                        number.pop(i)
                    number.append('1')
                    number.append('1')
                    number.append('0')
            else:
                i += 1
        answer.append(''.join(number))
    return answer

print(solution(["1110", "100111100", "0111111010"]))