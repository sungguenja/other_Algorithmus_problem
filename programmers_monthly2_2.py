memo = {}
def findAnswer(n):
    direct_answer = [1,2,3,4,5,6]
    if n <= 5:
        return direct_answer[n]
    original_bin = list(bin(n)[2:])
    othoer_bin = ['1'] + original_bin
    cnt = 1
    for i in range(1,len(othoer_bin)):
        if othoer_bin[i] == '1':
            othoer_bin[i] = '0'
            cnt += 1
            if cnt >= 2:
                break
    
    if original_bin[-1] == '0':
        original_bin[-1] = '1'
    else:
        for i in range(len(original_bin)-1,-1,-1):
            if original_bin[i] == '0':
                original_bin[i] = '1'
                original_bin[i+1] = '0'
                break
    original_bin = '0b'+''.join(original_bin)
    othoer_bin = '0b'+''.join(othoer_bin)
    original_bin = int(original_bin,2)
    othoer_bin = int(othoer_bin,2)
    if original_bin == n:
        return othoer_bin
    return min(original_bin,othoer_bin)


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(findAnswer(number))
    return answer
print(bin(995))
print(int('0b1111100101',2))