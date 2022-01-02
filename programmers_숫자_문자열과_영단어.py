number_speling = ['zero','one','two','three','four','five','six','seven','eight','nine']
def tStringNumberAndJump(s,i):
    if s[i:i+3] == number_speling[2]:
        return '2', 3
    elif s[i:i+5] == number_speling[3]:
        return '3', 5
    return '0', 1

def fStringNumberAndJump(s,i):
    if s[i:i+4] == number_speling[4]:
        return '4', 4
    elif s[i:i+4] == number_speling[5]:
        return '5', 4
    return '0', 1

def sStringNumberAndJump(s,i):
    if s[i:i+3] == number_speling[6]:
        return '6', 3
    elif s[i:i+5] == number_speling[7]:
        return '7', 5
    return '0', 1

def jumpStringAndGetNumber(s,i):
    if s[i] == 'z':
        return '0', 4
    elif s[i] == 'o':
        return '1', 3
    elif s[i] == 't':
        return tStringNumberAndJump(s,i)
    elif s[i] == 'f':
        return fStringNumberAndJump(s,i)
    elif s[i] == 's':
        return sStringNumberAndJump(s,i)
    elif s[i] == 'e':
        return '8', 5
    elif s[i] == 'n':
        return '9', 4
    return '0',1

def isNumber(i):
    number_string = [str(j) for j in range(10)]
    if i in number_string:
        return True
    return False

def solution(s):
    answer = ''
    i = 0
    while i < len(s):
        if isNumber(s[i]):
            answer += s[i]
            i += 1
            continue
        next_word, next_i = jumpStringAndGetNumber(s,i)
        answer += next_word
        i += next_i
    return int(answer)