# 이거 시간초과뜸
from collections import deque
N = int(input())
check = [-1]*(N+1)
check[N] = 0
answer = []
def makeOne(number):
    global answer
    Que = deque()
    Que.append([number,[str(number)]])
    while Que:
        now_number, now_array = Que.popleft()
        if now_number == 1:
            if answer == [] or len(answer) > len(now_array):
                answer = now_array
            continue
        if now_number%3 == 0:
            if check[now_number//3] == -1 or check[now_number//3] > check[now_number] + 1:
                check[now_number//3] = check[now_number] + 1
                Que.append([now_number//3,now_array+[str(now_number//3)]])
        if now_number%2 == 0:
            if check[now_number//2] == -1 or check[now_number//2] > check[now_number] + 1:
                check[now_number//2] = check[now_number] + 1
                Que.append([now_number//2,now_array+[str(now_number//2)]])
        if now_number > 1:
            if check[now_number - 1] == -1 or check[now_number - 1] > check[now_number] + 1:
                check[now_number - 1] = check[now_number] + 1
                Que.append([now_number-1,now_array+[str(now_number-1)]])

makeOne(N)
print(len(answer))
print(' '.join(answer))