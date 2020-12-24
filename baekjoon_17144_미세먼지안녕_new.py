import sys
N,M,T = map(int,sys.stdin.readline().split())
room = [0]*N
upper = []
lower = []
trigger = True
for i in range(N):
    horizion = list(map(int,sys.stdin.readline().split()))
    if trigger:
        if horizion[0] == -1:
            upper = [i,0]
            lower = [i+1,0]
            trigger = False
    room[i] = horizion[:]
di = [0,1,0,-1]
dj = [1,0,-1,0]
for t in range(T):
    diffusion = [[0]*M for i in range(N)]
    diffusion[upper[0]][upper[1]] = -1
    diffusion[lower[0]][lower[1]] = -1
    for i in range(N):
        for j in range(M):
            if room[i][j] > 0:
                cnt = 0
                diffused = room[i][j]//5
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<N and 0<=nj<M:
                        if room[ni][nj] != -1:
                            cnt += 1
                            diffusion[ni][nj] += diffused
                else:
                    diffusion[i][j] += -diffused*cnt
    for i in range(N):
        for j in range(M):
            if room[i][j] == -1:
                continue
            room[i][j] = diffusion[i][j]+room[i][j]
    upper_start_i = upper[0]-1
    upper_start_j = upper[1]
    lower_start_i = lower[0]+1
    lower_start_j = lower[1]
    while upper_start_i>0:
        room[upper_start_i][upper_start_j] = room[upper_start_i-1][upper_start_j]
        upper_start_i -= 1
    while upper_start_j<M-1:
        room[upper_start_i][upper_start_j] = room[upper_start_i][upper_start_j+1]
        upper_start_j += 1
    while upper_start_i<upper[0]:
        room[upper_start_i][upper_start_j] = room[upper_start_i+1][upper_start_j]
        upper_start_i += 1
    while upper_start_j>upper[1]+1:
        room[upper_start_i][upper_start_j] = room[upper_start_i][upper_start_j-1]
        upper_start_j -= 1
    
    while lower_start_i<N-1:
        room[lower_start_i][lower_start_j] = room[lower_start_i+1][lower_start_j]
        lower_start_i += 1
    while lower_start_j<M-1:
        room[lower_start_i][lower_start_j] = room[lower_start_i][lower_start_j+1]
        lower_start_j += 1
    while lower_start_i>lower[0]:
        room[lower_start_i][lower_start_j] = room[lower_start_i-1][lower_start_j]
        lower_start_i -= 1
    while lower_start_j>lower[1]+1:
        room[lower_start_i][lower_start_j] = room[lower_start_i][lower_start_j-1]
        lower_start_j -= 1
    room[upper[0]][upper[1]+1] = 0
    room[lower[0]][lower[1]+1] = 0
answer = 0
for i in range(N):
    for j in range(M):
        if room[i][j]>0:
            answer += room[i][j]
print(answer)