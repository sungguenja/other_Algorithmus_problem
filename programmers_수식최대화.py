from itertools import permutations
def solution(expression):
    answer = 0
    now = ''
    number = []
    calcul = []
    for i in range(len(expression)):
        if expression[i] == '*' or expression[i] == '+' or expression[i] == '-':
            number.append(int(now))
            now = ''
            calcul.append(expression[i])
        else:
            now += expression[i]
    else:
        number.append(int(now))
    case = list(permutations(set(calcul)))
    for i in range(len(case)):
        now_number = number[:]
        now_calcul = calcul[:]
        for j in case[i]:
            k=0
            while k<len(now_calcul):
                if j==now_calcul[k]:
                    now_case = now_calcul.pop(k)
                    number_1 = now_number.pop(k)
                    number_2 = now_number.pop(k)
                    if now_case == '+':
                        temp = number_1 + number_2
                    elif now_case == '-':
                        temp = number_1 - number_2
                    else:
                        temp = number_1 * number_2
                    now_number.insert(k,temp)
                else:
                    k+=1
        if answer < abs(now_number[0]):
            answer = abs(now_number[0])
    return answer