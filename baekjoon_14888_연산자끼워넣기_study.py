min_answer = 1000000000
max_answer = -1000000000
def solution(now,length,whe=1):
    global min_answer,max_answer
    if length == whe:
        if now < min_answer:
            min_answer = now
        if now > max_answer:
            max_answer = now
        return

    for i in range(len(count)):
        if count[i] > 0:
            count[i] -= 1
            if i == 0:
                solution(now+number[whe],length,whe+1)
            elif i == 1:
                solution(now-number[whe],length,whe+1)
            elif i == 2:
                solution(now*number[whe],length,whe+1)
            elif i == 3:
                if number[whe] != 0:
                    if now>=0:
                        solution(now//number[whe],length,whe+1)
                    else:
                        solution(-((-now)//number[whe]),length,whe+1)
            count[i] += 1

N = int(input())
number = list(map(int,input().split()))
count = list(map(int,input().split()))
solution(number[0],N)
print(max_answer)
print(min_answer)