L = int(input())
game = []
for _ in range(2*L+1):         # 게임판 만들기
    vertical = []
    vertical = [None]*(2*L+1)
    game.append(vertical)
snake = [L,L]                     # 첫 뱀 위치
game[L][L] = 0                  # 시작 구현
dk = [[0,1],[1,0],[0,-1],[-1,0]]    # 방향
k=0                             # 시작은 오른쪽을 본다
snake_len = 1
trigger = 0                     # 데스빔
for _ in range(int(input())):   # 명령어 수만큼
    command = input().split()
    length = int(command[0])
    direction = command[1]
    for z in range(length):
        snake[0] += dk[k][0]
        snake[1] += dk[k][1]
        try:
            if game[snake[0]][snake[1]] == None:
                game[snake[0]][snake[1]] = 0
                snake_len += 1
            else:
                trigger = 1         # 으앙주금
                break
        except IndexError:
            trigger = 1
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
    for z in game:
        print(z)
print(snake_len)

