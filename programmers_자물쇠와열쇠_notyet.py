def solution(key, lock):
    locker = []
    end = -1
    start = len(lock)*len(lock)+1
    num = 0
    for i in range(len(lock)):
        for j in range((len(lock))):
            locker.append((lock[i][j]+1)%2)
            if lock[i][j]==0:
                if num<start:
                    start=num
                if num>end:
                    end=num
            num+=1
    
    copy_key_000 = []
    copy_key_090 = []
    copy_key_180 = []
    copy_key_270 = []
    for i in range(len(key)):
        for j in range(len(key)):
            copy_key_000.append(key[i][j])
    for j in range(len(key)):
        for i in range(len(key)-1,-1,-1):
            copy_key_090.append(key[i][j])
    for i in range(len(key)):
        for j in range(len(key)-1,-1,-1):
            copy_key_180.append(key[i][j])
    for j in range(len(key)):
        for i in range(len(key)):
            copy_key_270.append(key[i][j])

    answer = False
    for k in range(len(copy_key_000)-(end-start)):
        if copy_key_000[k:k+(end-start)+1] == locker[start:end+1]:
            answer = True
        if copy_key_090[k:k+(end-start)+1] == locker[start:end+1]:
            answer = True
        if copy_key_180[k:k+(end-start)+1] == locker[start:end+1]:
            answer = True
        if copy_key_270[k:k+(end-start)+1] == locker[start:end+1]:
            answer = True
    
    return answer

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,1,0]]))