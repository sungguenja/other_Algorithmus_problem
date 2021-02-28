from copy import deepcopy

direction_i = [-1,-1,0,1,1,1,0,-1]
direction_j = [0,-1,-1,-1,0,1,1,1]

fishes = [list(map(int,input().split())) for i in range(4)]
aqua = [
    [[],[],[],[]],
    [[],[],[],[]],
    [[],[],[],[]],
    [[],[],[],[]]
]

fish_list = []
for fish_case in range(1,17):
    trigger = False
    for i in range(4):
        for j in range(4):
            if fishes[i][2*j] == fish_case:
                fish_list.append([fishes[i][2*j],i,j])
                trigger = True
                break
        if trigger:
            break

for i in range(4):
    for j in range(4):
        aqua[i][j] = [fishes[i][2*j],fishes[i][2*j+1]-1]

start_fish = aqua[0][0][0]
answer = start_fish
shark = [0,0,aqua[0][0][1]]
fish_list[start_fish-1] = -1
aqua[0][0] = -1 # 상어 있음 -1 물고기 없음 0

def move_fish(move_aquarium,move_status):
    for fish in range(16):
        if move_status[fish] == -1:
            continue
        i,j = move_status[fish][1],move_status[fish][2]
        d = move_aquarium[i][j][1]
        before_d = d
        ni = i + direction_i[d]
        nj = j + direction_j[d]
        trigger = False
        if 0<=ni<4 and 0<=nj<4 and move_aquarium[ni][nj] == -1:
            d = (d+1)%8
            ni = i + direction_i[d]
            nj = j + direction_j[d]
        
        while ni<0 or ni>=4 or nj<0 or nj>=4:
            d = (d+1)%8
            ni = i + direction_i[d]
            nj = j + direction_j[d]
            if 0<=ni<4 and 0<=nj<4 and move_aquarium[ni][nj] == -1:
                d = (d+1)%8
                ni = i + direction_i[d]
                nj = j + direction_j[d]
            if before_d == d:
                trigger = True
                break
        
        if trigger:
            continue
        
        if move_aquarium[ni][nj] == 0:
            move_status[fish] = [fish+1,ni,nj]
        else:
            after_fish = move_status[move_aquarium[ni][nj][0]-1][0]-1
            move_status[fish][1],move_status[fish][2],move_status[after_fish][1],move_status[after_fish][2] = move_status[after_fish][1],move_status[after_fish][2],move_status[fish][1],move_status[fish][2]
        move_aquarium[i][j],move_aquarium[ni][nj] = move_aquarium[ni][nj],[move_aquarium[i][j][0],d]
    return deepcopy(move_aquarium),deepcopy(move_status)

def solution(cnt,aquarium,fish_status,shark_status):
    global answer
    if cnt > answer:
        answer = cnt
    
    after_aquarium,after_fish_satus = move_fish(aquarium,fish_status)

    i,j,d = shark_status
    ni = i + direction_i[d]
    nj = j + direction_j[d]
    while 0<=ni<4 and 0<=nj<4:
        if after_aquarium[ni][nj] == -1 or after_aquarium[ni][nj] == 0:
            ni += direction_i[d]
            nj += direction_j[d]
            continue
        now_cnt = after_aquarium[ni][nj][0]
        now_dir = after_aquarium[ni][nj][1]
        now_aquarium = deepcopy(after_aquarium)
        now_aquarium[i][j] = 0
        now_fish_status = deepcopy(after_fish_satus)
        now_fish_status[now_cnt-1] = -1
        now_aquarium[ni][nj] = -1
        solution(cnt+now_cnt,deepcopy(now_aquarium),deepcopy(now_fish_status),[ni,nj,now_dir])
        ni += direction_i[d]
        nj += direction_j[d]

solution(answer,deepcopy(aqua),deepcopy(fish_list),deepcopy(shark))
print(answer)