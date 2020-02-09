vingo = []                                  # 빙고판
for _ in range(5):
    horizontal = []
    horizontal = list(map(int, input().split()))
    vingo.append(horizontal)

bingo = False                               # 빙고 체크용

calling = []                                # 사회자 순서
for _ in range(5):
    call_horizon = []
    call_horizon = list(map(int, input().split()))
    calling.append(call_horizon)

call_hor = 0                                # 호출용
call_ver = 0

calling_count = 0

while not bingo:
    counting = 0
    trigger = 0                        # 빙고 숫자 찾을 시 멈추는 용
    numb = calling[call_ver][call_hor]
    call_hor += 1
    calling_count += 1

    if call_hor == 5:                   # 가로줄 끝까지 불렀을 시
        call_hor = 0
        call_ver += 1
    
    for i in range(5):
        if trigger == 1:
            break
        for j in range(5):
            if vingo[i][j] == numb:     # 뷩고
                vingo[i][j] = 'X'
                trigger = 1
                break
    
    if vingo[0][0] == 'X' and vingo[1][1] == 'X' and vingo[2][2] == 'X' and vingo[3][3] == 'X' and vingo[4][4] == 'X':
        counting += 1
    if vingo[0][4] == 'X' and vingo[1][3] == 'X' and vingo[2][2] == 'X' and vingo[3][1] == 'X' and vingo[4][0] == 'X':
        counting += 1
    for i in range(5):
        if vingo[i][0] == 'X' and vingo[i][1] == 'X' and vingo[i][2] == 'X' and vingo[i][3] == 'X' and vingo[i][4] == 'X':
            counting += 1
    for j in range(5):
        if vingo[0][j] == 'X' and vingo[1][j] == 'X' and vingo[2][j] == 'X' and vingo[3][j] == 'X' and vingo[4][j] == 'X':
            counting += 1
    
    if counting >= 3:
        bingo = True

print(calling_count)