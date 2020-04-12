from copy import deepcopy
def rotate(cipher):
    c_cipher = deepcopy(cipher)
    for i in range(len(cipher)):
        for j in range(len(cipher)):
            c_cipher[j][len(cipher)-1-i] = cipher[i][j]
    return c_cipher

def check(y,x,cipher,field,door):
    c_field = deepcopy(field)
    for i in range(y,y+len(cipher)):
        for j in range(x,x+len(cipher)):
            c_field[i][j] += cipher[i-y][j-x]
    trigger = True
    for i in range(len(cipher)-1,len(cipher)-1+len(door)):
        for j in range(len(cipher)-1,len(cipher)-1+len(door)):
            if c_field[i][j] == 0 or c_field[i][j] == 2:
                trigger = False
                break
        if not trigger:
            break
    return trigger

def solution(key, lock):
    locker = [[0]*(2*(len(key)-1)+len(lock)) for _ in range(2*(len(key)-1)+len(lock))]
    
    for i in range(len(key)-1,len(key)-1+len(lock)):
        for j in range(len(key)-1,len(key)-1+len(lock)):
            locker[i][j] = lock[i-len(key)+1][j-len(key)+1]

    for _ in range(4):
        key = deepcopy(rotate(key))
        for i in range(len(key)+len(lock)-1):
            for j in range(len(key)+len(lock)-1):
                answer = check(i,j,key,locker,lock)
                if answer:
                    break
            if answer:
                break
        if answer:
            break

    return answer

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))