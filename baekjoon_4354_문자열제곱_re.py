def findSquared(now_string):
    result = 0
    length = len(now_string)

    if len(set(now_string)) == 1:
        return length
    
    for i in range(1,length//2+1):
        if length % i != 0:
            continue
        now_answer = length // i
        compare_string = now_string[:i]*now_answer
        if compare_string == now_string:
            result = max(now_answer,result)
    
    if result == 0:
        result = 1
        
    return result

while True:
    now_string = input()
    if now_string == '.':
        break
    print(findSquared(now_string))