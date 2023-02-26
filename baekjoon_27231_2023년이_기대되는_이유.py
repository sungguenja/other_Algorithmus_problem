def makeNumberArrayAndGetIsOnlyOneAndZero(innerNumber):
    isOnlyOneAndZero = True
    stringNumber = str(innerNumber)
    numberArray = []
    for i in stringNumber:
        numberArray.append(i)
        if i != '1' and i != '0':
            isOnlyOneAndZero = False
    
    return numberArray, isOnlyOneAndZero

def makeSqrtSumNumberArray(innerNumber):
    result = []
    for i in range(1,30):
        result.append(sum(list(map(lambda innerI: int(innerI) ** i, innerNumber))))
    return result

canGlobalList = set()

def makeNumberEachArray(innerNumber, start = 0, nowStr = '', tmp = []):
    global canGlobalList
    if (len(innerNumber) <= start):
        if (nowStr != ''):
            tmp.append(nowStr)
        if (len(''.join(tmp)) == len(innerNumber)):
            canGlobalList.add(sum(map(int,tmp)))   

    
    for i in range(start,len(innerNumber)):
        makeNumberEachArray(innerNumber, i + 1, nowStr + innerNumber[i], tmp[:])
        tmp.append(nowStr + innerNumber[i])
        makeNumberEachArray(innerNumber, i + 1, '', tmp[:])
        tmp.pop()

N = int(input())

for _ in range(N):
    canGlobalList = set()
    answer = 0
    nowNumber = int(input())
    numberArray, isOnlyOneAndZero = makeNumberArrayAndGetIsOnlyOneAndZero(nowNumber)
    if isOnlyOneAndZero:
        print('Hello, BOJ 2023!')
        continue
    canSumList = makeSqrtSumNumberArray(numberArray)
    makeNumberEachArray(numberArray)
    for i in canSumList:
        if (i in canGlobalList):
            answer += 1
    print(answer)