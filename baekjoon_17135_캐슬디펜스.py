import copy
NMD = list(map(int, input().split()))
N, M, D = NMD[0], NMD[1], NMD[2]
enemy = []
for _ in range(N):                              # 적 상황받기
    enemy_x = []
    enemy_x = list(map(int, input().split()))
    enemy.append(enemy_x)

arrow = []                                      # 궁수 배치
for i in range(0,M-2):
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            arrow_garo = [0]*M
            arrow_garo[i] = 'i'
            arrow_garo[j] = 'j'
            arrow_garo[k] = 'k'
            arrow.append(arrow_garo)

enemy_kill_count = 0      # 게임 진행, 적을 찾아서 거리랑 왼쪽 생각 적을 옮기자
enemy_save = enemy
enemy_kill = 0
for n in arrow:
    enemy = copy.deepcopy(enemy_save)
    enemy.append(n)   # 궁수 자리 배치
    ill_kill, jll_kill, kll_kill = [], [], []
    Di, Dj, Dk = N+M, N+M, N+M
    if enemy_kill_count < enemy_kill:
        enemy_kill_count = enemy_kill
    enemy_kill = 0
    while enemy[:N] != [[0]*M]*N:
        for i in range(N):
            for j in range(M):
                if enemy[i][j] == 1: # I've got you in my sight
                    Di_imsi = abs(i-N)+abs(j-enemy[N].index('i'))
                    Dj_imsi = abs(i-N)+abs(j-enemy[N].index('j'))
                    Dk_imsi = abs(i-N)+abs(j-enemy[N].index('k'))
                    if D >= Di_imsi and Di >= Di_imsi:
                        if ill_kill == []:  # 목표가 첫 목표일경우
                            Di = Di_imsi
                            ill_kill.append([i,j])
                        else:
                            if Di>Di_imsi:    # 다른 목표를 포착했다
                                ill_kill.pop()
                                ill_kill.append([i,j])
                                Di = Di_imsi
                            elif Di==Di_imsi:
                                if ill_kill[0][1] > j:
                                    ill_kill.pop()
                                    ill_kill.append([i,j])
                                    Di = Di_imsi
                    if D >= Dj_imsi and Dj >= Dj_imsi:
                        if jll_kill == []:
                            Dj = Dj_imsi
                            jll_kill.append([i,j])
                        else:
                            if Dj>Dj_imsi:    # 다른 목표를 포착했다
                                jll_kill.pop()
                                jll_kill.append([i,j])
                                Dj = Dj_imsi
                            elif Dj==Dj_imsi:
                                if jll_kill[0][1] > j:
                                    jll_kill.pop()
                                    jll_kill.append([i,j])
                                    Dj = Dj_imsi
                    if D >= Dk_imsi and Dk >= Dk_imsi:
                        if kll_kill == []:
                            Dk = Dk_imsi
                            kll_kill.append([i,j])
                        else:
                            if Dk>Dk_imsi:    # 다른 목표를 포착했다
                                kll_kill.pop()
                                kll_kill.append([i,j])
                                Dk = Dk_imsi
                            elif Dk==Dk_imsi:
                                if kll_kill[0][1] > j:
                                    kll_kill.pop()
                                    kll_kill.append([i,j])
                                    Dk = Dk_imsi
        if ill_kill != []:                  # 적을 발견했는가? 죽여
            enemy[ill_kill[0][0]][ill_kill[0][1]] = 0
            enemy_kill += 1
        if jll_kill != [] and enemy[jll_kill[0][0]][jll_kill[0][1]] != 0:
            enemy[jll_kill[0][0]][jll_kill[0][1]] = 0 # 전 당번이 죽이면 못죽임
            enemy_kill += 1
        if kll_kill != [] and enemy[kll_kill[0][0]][kll_kill[0][1]] != 0:
            enemy[kll_kill[0][0]][kll_kill[0][1]] = 0
            enemy_kill += 1
        for z in range(N-1,0,-1):      # 거꾸로 해줘야 안전하게 옮긴다
            enemy[z] = enemy[z-1]      # 근데 그냥 스왑으로 될 거 같기도 한데
        enemy[0] = [0]*M          # 첫자리엔 없어야맞지
        if ill_kill != []:
            ill_kill.pop()            # pop을 밖에 넣어줘야 한다
        if jll_kill != []:
            jll_kill.pop()            # 혹시 걸러지는 경우를 건져낼 수 있음
        if kll_kill != []:
            kll_kill.pop()
print(enemy_kill_count)
# 거리가 이상함