gear = [0]*4    # 톱니바퀴
gear[0] = list(map(int,list(input())))
gear[1] = list(map(int,list(input())))
gear[2] = list(map(int,list(input())))
gear[3] = list(map(int,list(input())))
N = int(input())
command = [0]*N # 명령어
for i in range(N):
    command[i] = list(map(int,input().split()))

for i in range(N):
    position, direction = command[i]
    position -= 1
    check = [0]*4       # 도는지 여부를 체크하기 위한 용도
    check[position] = direction
    now_direction = direction   # 각자 도는 거
    for j in range(position,3): # 뒤로 체크하기
        now_direction *= -1
        if gear[j][2] != gear[j+1][6]:
            check[j+1] = now_direction
        else:
            break
    now_direction = direction
    for j in range(position,0,-1):  # 앞으로 체크하기
        now_direction *= -1
        if gear[j][6] != gear[j-1][2]:
            check[j-1] = now_direction
        else:
            break
    
    for j in range(4):
        if check[j] == 1:
            saving = gear[j][-1]
            for k in range(7,0,-1):
                gear[j][k] = gear[j][k-1]
            gear[j][0] = saving
        elif check[j] == -1:
            saving = gear[j][0]
            for k in range(0,7):
                gear[j][k] = gear[j][k+1]
            gear[j][7] = saving

answer = 0
for i in range(4):
    answer += gear[i][0]*(2**i)
print(answer)