def solution(word):
    alpha = ['A','E','I','O','U']
    answer = 0
    for i in range(len(word)):
        for j in range(5):
            if word[i] != alpha[j]:
                if i == 0:
                    answer += 781
                elif i == 1:
                    answer += 156
                elif i == 2:
                    answer += 31
                elif i == 3:
                    answer += 6
                elif i == 4:
                    answer += 1
            else:
                answer += 1
                break
    return answer