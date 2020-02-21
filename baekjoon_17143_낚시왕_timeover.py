import copy
R,C,M=map(int,input().split())

fishing = [[0]*C for _ in range(R)]     # 낚시터

shark = []                              # 상어 상태 저장용
for i in range(M):
    y,x,s,d,z=map(int,input().split())
    fishing[y-1][x-1] = [i,z]      # 몇번째 상어인지 기억하기 위한 용
    shark.append([i,s,d])

num = 0                            # 낚시꾼 시작
catch_shark = 0                    # 낚시한 양
while num<C:
    if M==0:      # 끝내는 조건: 잡을게 없다
        break
    for j in range(R):
        if fishing[j][num] != 0:
            catch_shark += fishing[j][num][1]
            shark[fishing[j][num][0]] = 0
            fishing[j][num] = 0
            break
    num += 1

    if shark == [0]*M: #끝내는 조건2:모든 상어는 상어의 뱃속에 있거나 망에 있거나
        break
    move_fish = [[0]*C for _ in range(R)]   # 복사본
    for fish in range(M):
        if shark[fish] == 0:
            continue
        else:
            for i in range(R):
                if type(shark[fish]) == int:    # 먹혔을시
                    break
                for j in range(C):
                    if type(shark[fish]) == int:
                        break
                    elif type(fishing[i][j]) != int and fishing[i][j][0] == shark[fish][0]:
                        y=i                 # 복사본에서 움직이기 위해
                        x=j
                        if shark[fish][2] == 1:
                            y -= shark[fish][1]
                            while y<0 or y>=R:
                                if y<0:
                                    y=y*(-1)
                                    shark[fish][2] = 2
                                elif y>=R:
                                    y=2*R-2-y
                                    shark[fish][2] = 1
                        elif shark[fish][2] == 2:
                            y += shark[fish][1]
                            while y<0 or y>=R:
                                if y<0:
                                    y=y*(-1)
                                    shark[fish][2] = 2
                                elif y>=R:
                                    y=2*R-2-y
                                    shark[fish][2] = 1
                        elif shark[fish][2] == 3:
                            x += shark[fish][1]
                            while x<0 or x>=C:
                                if x<0:
                                    x=x*(-1)
                                    shark[fish][2] = 3
                                elif x>=C:
                                    x=2*C-2-x
                                    shark[fish][2] = 4
                        elif shark[fish][2] == 4:
                            x -= shark[fish][1]
                            while x<0 or x>=C:
                                if x<0:
                                    x=x*(-1)
                                    shark[fish][2] = 3
                                elif x>=C:
                                    x=2*C-2-x
                                    shark[fish][2] = 4
                        
                        if move_fish[y][x] == 0:
                            move_fish[y][x] = copy.copy(fishing[i][j])
                        else:
                            if move_fish[y][x][1] < fishing[i][j][1]:
                                move_fish[y][x] = copy.copy(fishing[i][j])
                                shark[move_fish[y][x][0]] = 0
                            else:
                                shark[fishing[i][j][0]] = 0
    else:
        fishing = copy.deepcopy(move_fish)
print(catch_shark)