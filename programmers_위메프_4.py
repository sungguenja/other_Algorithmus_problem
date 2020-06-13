opened = ['[','(','{']
closed = [']',')','}']
def solution(text):
    answer = ''
    rank = 0
    word_list = dict()
    stack = []
    max_rank = -1
    for i in text:
        if i == ' ':
            continue
        if i in closed:
            word = ''
            while stack != []:
                j = stack.pop()
                if j in opened:
                    word_list[word] = rank
                    if rank>max_rank:
                        max_rank = rank
                    rank -= 1
                    break
                word = j+word
        else:
            if i in opened:
                trigger = True
                for j in opened:
                    if j in stack:
                        trigger = False
                        break
                if trigger:
                    word = ''
                    for j in stack:
                        word = word + j
                    stack = []
                    rank = 0
                    word_list[word] = rank
                rank += 1
            stack.append(i)
    if stack != []:
        word = ''
        for i in stack:
            if i in opened:
                continue
            word = word+i
        word_list[word] = 0
        print(word)
    print(word_list,max_rank)
    for i in range(max_rank,-1,-1):
        for key, value in word_list.items():
            if value == i:
                if key == '':
                    continue
                answer += key+','
    return answer[:-1]

print(solution('((아디다스) 무료 (나이키 (풋살화)) 배송) 강남점 (축구)(잔디)'))
print(solution('[지이크]신원'))
print(solution('(냉장고 (양문냉장고 (2형 (삼성전자 {nt3058}))))'))