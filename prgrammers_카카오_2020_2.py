operator = ['+','-','*']
def solution(expression):
    answer = 0
    rank = [['*','+','-'],['*','-','+'],['+','*','-'],['+','-','*'],['-','+','*'],['-','*','+']]
    number_list = []
    operator_list = []
    save_i = 0
    for i in range(len(expression)):
        if expression[i] in operator:
            number_list.append(int(expression[save_i:i]))
            operator_list.append(expression[i])
            save_i = i+1
    number_list.append(int(expression[save_i:]))
    save_list = number_list[:]
    save_operator = operator_list[:]
    save_expression = expression
    for i in range(len(rank)):
        number_list = save_list[:]
        expression = save_expression
        operator_list = save_operator[:]
        while operator_list != []:
            if rank[i][0] in operator_list:
                where = operator_list.index(rank[i][0])
                operator_list.pop(where)
                if rank[i][0] == '*':
                    number_list[where] = number_list[where]*number_list[where+1]
                    number_list.pop(where+1)
                elif rank[i][0] == '+':
                    number_list[where] = number_list[where]+number_list[where+1]
                    number_list.pop(where+1)
                elif rank[i][0] == '-':
                    number_list[where] = number_list[where]-number_list[where+1]
                    number_list.pop(where+1)
            elif rank[i][1] in operator_list:
                where = operator_list.index(rank[i][1])
                operator_list.pop(where)
                if rank[i][1] == '*':
                    number_list[where] = number_list[where]*number_list[where+1]
                    number_list.pop(where+1)
                elif rank[i][1] == '+':
                    number_list[where] = number_list[where]+number_list[where+1]
                    number_list.pop(where+1)
                elif rank[i][1] == '-':
                    number_list[where] = number_list[where]-number_list[where+1]
                    number_list.pop(where+1)
            elif rank[i][2] in operator_list:
                where = operator_list.index(rank[i][2])
                operator_list.pop(where)
                if rank[i][2] == '*':
                    number_list[where] = number_list[where]*number_list[where+1]
                    number_list.pop(where+1)
                elif rank[i][2] == '+':
                    number_list[where] = number_list[where]+number_list[where+1]
                    number_list.pop(where+1)
                elif rank[i][2] == '-':
                    number_list[where] = number_list[where]-number_list[where+1]
                    number_list.pop(where+1)
        if answer == 0 or answer<abs(number_list[0]):
            answer = abs(number_list[0])

    return answer

print(solution("100-200*300-500+20"))