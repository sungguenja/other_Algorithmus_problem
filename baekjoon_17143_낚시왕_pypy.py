import copy
R,C,M=map(int,input().split())

fishing = [[0]*C for _ in range(R)]     # 낚시터

shark = []                              # 상어 상태 저장용
for i in range(M):
    y,x,s,d,z=map(int,input().split())
    fishing[y-1][x-1] = [i,z]      # 몇번째 상어인지 기억하기 위한 용
    shark.append([i,s,d,y-1,x-1])
                          # 낚시꾼 시작
catch_shark = 0                    # 낚시한 양
for num in range(C):
    if M==0:      # 끝내는 조건: 잡을게 없다
        break
    for j in range(R):
        if fishing[j][num] != 0:
            catch_shark += fishing[j][num][1]
            shark[fishing[j][num][0]] = 0
            fishing[j][num] = 0
            break

    if shark == [0]*M: #끝내는 조건2:모든 상어는 상어의 뱃속에 있거나 망에 있거나
        break
    move_fish = [[0]*C for _ in range(R)]   # 복사본
    for fish in range(M):
        if shark[fish] == 0:
            continue
        else:
            ni, nj = shark[fish][3], shark[fish][4] # 위치 복사
            if shark[fish][2] == 1:                 # 방향에 따른 움직임
                ni -= shark[fish][1]
                while ni<0 or ni>=R:
                    if ni<0:
                        ni=ni*(-1)
                        shark[fish][2] = 2
                    elif ni>=R:
                        ni=2*R-2-ni
                        shark[fish][2] = 1
            elif shark[fish][2] == 2:
                ni += shark[fish][1]
                while ni<0 or ni>=R:
                    if ni<0:
                        ni=ni*(-1)
                        shark[fish][2] = 2
                    elif ni>=R:
                        ni=2*R-2-ni
                        shark[fish][2] = 1
            elif shark[fish][2] == 3:
                nj += shark[fish][1]
                while nj<0 or nj>=C:
                    if nj<0:
                        nj=nj*(-1)
                        shark[fish][2] = 3
                    elif nj>=C:
                        nj=2*C-2-nj
                        shark[fish][2] = 4
            elif shark[fish][2] == 4:
                nj -= shark[fish][1]
                while nj<0 or nj>=C:
                    if nj<0:
                        nj=nj*(-1)
                        shark[fish][2] = 3
                    elif nj>=C:
                        nj=2*C-2-nj
                        shark[fish][2] = 4
            
            if move_fish[ni][nj] == 0:          # 빈 곳이다
                move_fish[ni][nj] = copy.copy(fishing[shark[fish][3]][shark[fish][4]])
                shark[fish][3], shark[fish][4] = ni, nj
            else:
                if move_fish[ni][nj][1] < fishing[shark[fish][3]][shark[fish][4]][1]:                   # 도착했는데 원래 있던 놈이 작음
                    shark[move_fish[ni][nj][0]] = 0
                    move_fish[ni][nj] = copy.copy(fishing[shark[fish][3]][shark[fish][4]])      # 먹어버림
                    shark[fish][3], shark[fish][4] = ni, nj
                    
                else:
                    shark[fishing[shark[fish][3]][shark[fish][4]][0]] = 0
    else:
        fishing = copy.deepcopy(move_fish)
print(catch_shark)