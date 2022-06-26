from copy import deepcopy
di = [0,0,-1,-1,-1,0,1,1,1]
dj = [0,-1,-1,0,1,1,1,0,-1]
water_checker_di = [-1,-1,1,1]
water_checker_dj = [-1,1,-1,1]
def getArrivalPosition(position,now_moving,size):
    direction,move_length = now_moving
    if move_length >= size:
        move_length = move_length % size
    i,j = position
    ni = i + (di[direction] * move_length)
    nj = j + (dj[direction] * move_length)
    while ni < 0 or ni >= size:
        if ni < 0:
            ni += size
        elif ni >= size:
            ni -= size
    while nj < 0 or nj >= size:
        if nj < 0:
            nj += size
        elif nj >= size:
            nj -= size
    return [ni,nj]

def makeNewCloud(now_water_board,size,now_cloud):
    return_cloud = []
    for i in range(size):
        for j in range(size):
            if now_water_board[i][j] >= 2 and not now_cloud[i][j]:
                now_water_board[i][j] -= 2
                return_cloud.append([i,j])
    return deepcopy(return_cloud),deepcopy(now_water_board)

N,M = map(int,input().split())
water_board = [list(map(int,input().split())) for _ in range(N)]
move_situation = [list(map(int,input().split())) for _ in range(M)]
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
for now_move in range(M):
    cloud_in_board = [[False]*N for _ in range(N)] # 구름 유무의 판별을 위한 어레이, 메모리를 쓰더라도 position in cloud 같은 연산보다 빠르게 작동하기 위해 이용
    for cl in range(len(cloud)):
        cloud[cl] = getArrivalPosition(cloud[cl],move_situation[now_move],N)
        i,j = cloud[cl]
        water_board[i][j] += 1
        cloud_in_board[i][j] = True

    for cl in range(len(cloud)):
        i,j = cloud[cl]
        checker = 0
        for k in range(4):
            ni = i + water_checker_di[k]
            nj = j + water_checker_dj[k]
            if 0<=ni<N and 0<=nj<N and water_board[ni][nj] > 0:
                checker += 1
        if checker > 0:
            water_board[i][j] += checker
    cloud, water_board = makeNewCloud(water_board,N,cloud_in_board)

answer = 0
for water in water_board:
    answer += sum(water)

print(answer)