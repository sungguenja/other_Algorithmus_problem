# 게임판 만들었더니 메모리터지는거 같다
L=int(input())
dk = [[0,1],[1,0],[0,-1],[-1,0]]    # 방향
k=0                             # 시작은 오른쪽을 본다
snake = [0,0]                 # 시작점, 지나간 자리를 저장하는 방식으로 한다
stack = [[0,0]]
snake_len = 1
trigger = 0                     # 데스빔
for _ in range(int(input())):   # 명령어 수만큼
    command = input().split()
    length = int(command[0])
    direction = command[1]
    for z in range(length):
        if ([snake[0]+dk[k][0],snake[1]+dk[k][1]] in snake) or (abs(snake[0]+dk[k][0])<=L) or (abs(snake[1]+dk[k][1])<=L):
            trigger = 1         # 자기몸위에 도착하거나 판을 나갈 때, 으앙 주금
        else:                   
            stack.append([snake[0]+dk[k][0],snake[1]+dk[k][1]])
            snake_len += 1      # 지나가지 않았고 판밖을 나가지 않을때
            snake[0] += dk[k][0]
            snake[1] += dk[k][1]
            break    
    if trigger == 1:
        break
    if direction == 'L':
        k -= 1
        if k == 0:
            k=3
    else:
        k += 1
        if k == 4:
            k=0
print(snake_len)