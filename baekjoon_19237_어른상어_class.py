from copy import deepcopy
class Shark:
    def __init__(self,position,number,direction=None,direction_list=None):
        self.position = position
        self.number = number
        self.direction = direction
        self.direction_list = direction_list

# 1위 2아래 3왼쪽 4오른쪽
di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]

N,M,K = map(int,input().split())
shark_cnt = M
aqua = [list(map(int,input().split())) for i in range(N)]
smell = [[-1]*N for i in range(N)]
shark_list = [0]*(M+1)
for i in range(N):
    for j in range(N):
        if aqua[i][j] != 0:
            shark_list[aqua[i][j]] = Shark((i,j),aqua[i][j])
            smell[i][j] = [aqua[i][j],K]

direction_situation = [0]+list(map(int,input().split()))
for i in range(1,M+1):
    shark_list[i].direction = direction_situation[i]

for i in range(M):
    direction_list = [0]
    for j in range(4):
        direction_list.append(list(map(int,input().split())))
    shark_list[i+1].direction_list = direction_list

def move_shark():
    global aqua,smell,N,M,shark_cnt
    after_aqua = [[0]*N for i in range(N)]
    after_smell = deepcopy(smell)
    for shark in shark_list:
        if shark == 0:
            continue
        shark_i,shark_j = shark.position
        for direct in shark.direction_list[shark.direction]:
            after_i = shark_i + di[direct]
            after_j = shark_j + dj[direct]
            if 0<=after_i<N and 0<=after_j<N and smell[after_i][after_j] == -1:
                after_aqua,after_smell = move_now((shark_i,shark_j),(after_i,after_j),after_aqua,after_smell,shark.number,direct)
                break
        else:
            for direct in shark.direction_list[shark.direction]:
                after_i = shark_i + di[direct]
                after_j = shark_j + dj[direct]
                if 0<=after_i<N and 0<=after_j<N and (type(smell[after_i][after_j]) == list and smell[after_i][after_j][0] == shark.number):
                    after_aqua,after_smell = move_now((shark_i,shark_j),(after_i,after_j),after_aqua,after_smell,shark.number,direct)
                    break
    
    aqua = deepcopy(after_aqua)
    smell = deepcopy(after_smell)

def move_now(before_position,after_position,after_aqua,after_smell,shark_number,direction):
    global shark_list,shark_cnt,K
    if after_aqua[after_position[0]][after_position[1]] == 0:
        after_aqua[after_position[0]][after_position[1]] = shark_number
        shark_list[shark_number].position = after_position
        shark_list[shark_number].direction = direction
        after_smell[after_position[0]][after_position[1]] = [shark_number,K+1]
    elif after_aqua[after_position[0]][after_position[1]] < shark_number:
        shark_cnt -= 1
        shark_list[shark_number] = 0
    elif after_aqua[after_position[0]][after_position[1]] > shark_number:
        shark_cnt -= 1
        died_shark_number = after_aqua[after_position[0]][after_position[1]]
        shark_list[died_shark_number] = 0
        shark_list[shark_number].position = after_position
        shark_list[shark_number].direction = direction
        after_aqua[after_position[0]][after_position[1]] = shark_number
        after_smell[after_position[0]][after_position[1]] = [shark_number,K+1]
    return after_aqua,after_smell

def perfum():
    global smell,N
    for i in range(N):
        for j in range(N):
            if smell[i][j] != -1:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = -1

for t in range(1,1002):
    if t>1000:
        break

    move_shark()
    perfum()

    if shark_cnt == 1:
        break

if t > 1000:
    t = -1
print(t)