from copy import deepcopy
N,M,K = map(int,input().split())
aqua = [list(map(int,input().split())) for i in range(N)]
shark_cnt = M
smell = deepcopy(aqua)
shark_position = [0]*(M+1)
for i in range(N):
    for j in range(N):
        if smell[i][j] == 0:
            smell[i][j] = -1
        else:
            smell[i][j] = [smell[i][j],K]
            shark_position[smell[i][j][0]] = [i,j]

# 1위 2아래 3왼쪽 4오른쪽
di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]
direction_list = [[0] for i in range(M+1)]
shark_direction = [0] + list(map(int,input().split()))
for i in range(4*M):
    direction_situation = list(map(int,input().split()))
    direction_list[i//4 + 1].append(direction_situation)

def move_shark():
    global aqua,N,M,smell
    # 후상황 기록용
    after_aqua = deepcopy(aqua)
    after_smell = deepcopy(smell)
    for shark in range(1,M+1):
        # 죽은 상어면 다음걸로 바로
        if shark_position[shark] == 0:
            continue
        shark_i,shark_j = shark_position[shark]
        for direction in direction_list[shark][shark_direction[shark]]:
            after_i = shark_i + di[direction]
            after_j = shark_j + dj[direction]
            # 도착지점 상황
            if 0<=after_i<N and 0<=after_j<N and smell[after_i][after_j] == -1:
                after_aqua,after_smell = move_situation(shark,shark_i,shark_j,after_i,after_j,after_aqua,direction,after_smell)
                break
        # 다 돌았지만 갈 수 있는 곳이 없을때
        else:
            for direction in direction_list[shark][shark_direction[shark]]:
                after_i = shark_i + di[direction]
                after_j = shark_j + dj[direction]
                if 0<=after_i<N and 0<=after_j<N and type(smell[after_i][after_j]) == list and smell[after_i][after_j][0] == shark:
                    after_aqua,after_smell = move_situation(shark,shark_i,shark_j,after_i,after_j,after_aqua,direction,after_smell)
                    break
    # 모두 옮겨졌으니 후상황 저장
    aqua = deepcopy(after_aqua)
    smell = deepcopy(after_smell)

def move_situation(shark,before_i,before_j,after_i,after_j,after_aqua,direction,after_smell):
    global shark_cnt
    # 아직 아무도 없을때
    if after_aqua[after_i][after_j] == 0:
        after_smell[after_i][after_j] = [shark,K+1]
        after_aqua[before_i][before_j] = 0
        after_aqua[after_i][after_j] = shark
        shark_direction[shark] = direction
        shark_position[shark] = [after_i,after_j]
    # 누군가 있는 상황이지만 내가 더 작은 숫자일때
    elif after_aqua[after_i][after_j] > shark:
        after_smell[after_i][after_j] = [shark,K+1]
        after_aqua[before_i][before_j] = 0
        died_shark = after_aqua[after_i][after_j]
        after_aqua[after_i][after_j] = shark
        shark_cnt -= 1
        shark_direction[shark] = direction
        shark_position[shark] = [after_i,after_j]
        shark_position[died_shark] = 0
    # 누군가 있는 상황이지만 내가 더 큰 숫자일때
    elif after_aqua[after_i][after_j] < shark:
        after_aqua[before_i][before_j] = 0
        died_shark = shark
        shark_cnt -= 1
        shark_direction[shark] = direction
        shark_position[died_shark] = 0
    return after_aqua,after_smell

def perfum():
    global smell,N
    for i in range(N):
        for j in range(N):
            if type(smell[i][j]) == list:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = -1

if M > 1:
    for t in range(1,1002):
        if t>1000:
            break

        move_shark()
        perfum()

        if shark_cnt == 1:
            break
else:
    t = 0

if t>1000:
    t = -1
print(t)