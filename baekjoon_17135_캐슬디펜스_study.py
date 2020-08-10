from copy import deepcopy
direction = [[0,-1],[-1,0],[0,1]]
N,M,D = map(int,input().split())
game = [list(map(int,input().split())) for _ in range(N)]
# 경우의 수 저장용
arrow = []
for i in range(M-2):
    for j in range(i+1,M-1):
        for k in range(j+1,M):
            arrow.append([i,j,k])

kill_enemy_maximum = -1
# 경우의 수 다 돌기
end_game = [[0]*M for _ in range(N)]
for case in range(len(arrow)):
    after_game = deepcopy(game)
    kill_count = 0
    while after_game != end_game:
        kill_case = []
        for t in range(3):
            visit = [[0]*M for _ in range(N)]
            Que = [[N,arrow[case][t],0]]
            trigger = False
            while Que != []:
                i,j,d = Que.pop(0)
                if d>=D:
                    continue
                for k in range(3):
                    ni = i+direction[k][0]
                    nj = j+direction[k][1]
                    if 0<=ni<N and 0<=nj<M:
                        if after_game[ni][nj] == 1:
                            if [ni,nj] not in kill_case:
                                kill_case.append([ni,nj])
                            trigger = True
                            break
                        elif after_game[ni][nj] == 0 and visit[ni][nj] == 0:
                            visit[ni][nj] = 1
                            Que.append([ni,nj,d+1])
                if trigger:
                    break
        for i in range(len(kill_case)):
            kill_count += 1
            after_game[kill_case[i][0]][kill_case[i][1]] = 0
        for i in range(N-1,0,-1):
            after_game[i] = after_game[i-1][:]
        after_game[0] = [0]*M
    if kill_enemy_maximum<kill_count:
        kill_enemy_maximum = kill_count
print(kill_enemy_maximum)