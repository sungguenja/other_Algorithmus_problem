import copy

NMD = list(map(int, input().split()))           #N,M,D 인풋
N,M,D = NMD[0], NMD[1], NMD[2]
enemy=[]                                        #진행을 위한 게임판
enemy_save=[]                                   #리셋을 위한 저장용
for _ in range(N):
    enemy_garo = []
    enemy_garo = list(map(int, input().split()))
    enemy.append(enemy_garo)
    enemy_save.append(enemy_garo)

arrow = []                                      #궁수배치
for i in range(M-2):
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            arrow_garo=[0]*M
            arrow_garo[i] = 'i'
            arrow_garo[j] = 'j'
            arrow_garo[k] = 'k'
            arrow.append(arrow_garo)

kill_count_save = 0                             # 카운팅 저장용
kill_count = 0                                  # 매판 킬 수 새는 용
for n in arrow:                                 # 게임진행
    enemy = copy.deepcopy(enemy_save)                       # 게임판 리셋
    enemy.append(n)                             # 궁수배치판 포함
    target = [['0','0'],['0','0'],['0','0']] # 목표 저장용
    kill_count = 0
    while enemy[:N] != [[0]*M]*N:               # 게임이 끝난 것인지 판단하자
        Di, Dj, Dk = N*M, N*M, N*M              # 거리저장용
        for i in range(N):
            for j in range(M):
                if enemy[i][j] == 1:                # I've got u in my sight
                    Di_imsi = abs(N-i)+abs(enemy[N].index('i')-j) #적과 궁수 거리
                    Dj_imsi = abs(N-i)+abs(enemy[N].index('j')-j)
                    Dk_imsi = abs(N-i)+abs(enemy[N].index('k')-j)
                    if D>=Di_imsi and Di>=Di_imsi: # 사거리 + 가장가까운 적 포착
                        if target[0] == ['0','0']:         # 처음 포착한 적?
                            target[0] = [i,j]
                            Di=Di_imsi
                        else:
                            if Di == Di_imsi:   # 포착한 적이 전 적과 거리가 같냐
                                if target[0][1] > j: #같으면 더 왼쪽인가
                                    target[0] = [i,j]
                                    Di = Di_imsi
                            elif Di > Di_imsi:    # 다르면 더 짧음?
                                target[0] =[i,j]
                                Di = Di_imsi
                    if D>=Dj_imsi and Dj>=Dj_imsi: # 사거리 + 가장가까운 적 포착
                        if target[1] == ['0','0']:         # 처음 포착한 적?
                            target[1] = [i,j]
                            Dj=Dj_imsi
                        else:
                            if Dj == Dj_imsi:   # 포착한 적이 전 적과 거리가 같냐
                                if target[1][1] > j: #같으면 더 왼쪽인가
                                    target[1] = [i,j]
                                    Dj = Dj_imsi
                            elif Dj > Dj_imsi:    # 다르면 더 짧음?
                                target[1] =[i,j]
                                Dj = Dj_imsi
                    if D>=Dk_imsi and Dk>=Dk_imsi: # 사거리 + 가장가까운 적 포착
                        if target[2] == ['0','0']:         # 처음 포착한 적?
                            target[2] = [i,j]
                            Dk=Dk_imsi
                        else:
                            if Dk == Dk_imsi:   # 포착한 적이 전 적과 거리가 같냐
                                if target[2][1] > j: #같으면 더 왼쪽인가
                                    target[2] = [i,j]
                                    Dk = Dk_imsi
                            elif Dk > Dk_imsi:    # 다르면 더 짧음?
                                target[2] =[i,j]
                                Dk = Dk_imsi
        for z in range(3):                      # 타겟 확인
            if target[z] != ['0','0']:          # 타겟을 포착했는가
                if enemy[target[z][0]][target[z][1]] != 0:  #이미 전사람이 쐈나
                    enemy[target[z][0]][target[z][1]] = 0
                    kill_count += 1
                target[z] = ['0','0']           # 쏴도 안쏴도 리셋
        for z in range(N-1,0,-1):               # 적 이동
            enemy[z] = enemy[z-1]               # 거꾸로 하는게 좋은거 같다
        enemy[0] = [0]*M                        # 맨 위는 적이 없다
    enemy.pop()
    if kill_count_save < kill_count:
        kill_count_save = kill_count
print(kill_count_save)