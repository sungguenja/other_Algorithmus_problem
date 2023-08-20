def solution(matchstick):
    answerMax = '7' * (matchstick % 2) + '1' * ((matchstick // 2) - (matchstick % 2))
    
    answerMin = ''
    useMatchstickCnt = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    if matchstick <= 10:
        answerMin = useMatchstickCnt[matchstick]
    else:
        while matchstick > 0:
            matchstick -= 7
            if matchstick >= 0:
                answerMin += '8'
            else:
                matchstick += 7
                break

            
        if matchstick == 1:
            answerMin = '10' + answerMin[1:]
        elif matchstick == 2:
            answerMin = '1' + answerMin
        elif matchstick == 3:
            answerMin = '200' + answerMin[2:]
        elif matchstick == 4:
            answerMin = '20' + answerMin[1:]
        elif matchstick == 5:
            answerMin = '2' + answerMin
        elif matchstick == 6:
            answerMin = '6' + answerMin
        
        
    return str(answerMin) + ' ' + str(answerMax)

N = int(input())
numberList = [int(input()) for _ in range(N)]

for matchstick in numberList:
    print(solution(matchstick))