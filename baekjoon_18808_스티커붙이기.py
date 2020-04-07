from copy import deepcopy

N,M,S=map(int,input().split())
paper = [[0]*M for _ in range(N)]
sticker = [[0]*4 for _ in range(S)]
for i in range(S):
    y,x=map(int,input().split())
    now_sticker=[0]*y
    for j in range(y):
        horizone = []
        horizone = list(map(int,input().split()))
        now_sticker[j] = horizone[:]
    zero_degree = deepcopy(now_sticker)
    ninty_degre = [[0]*N for _ in range(M)]
    reverse_deg = [[0]*N for _ in range(M)]
    pi_degree = [[0]*M for _ in range(N)]
    for ni in range(N):
        for nj in range(M):
            ninty_degre[nj][ni] = zero_degree[ni][nj]
            reverse_deg[-nj-1][-ni-1] = zero_degree[ni][nj]
            pi_degree[-ni-1][-nj-1] = zero_degree[ni][nj]
    sticker[i][0] = deepcopy(zero_degree)
    sticker[i][1] = deepcopy(ninty_degre)
    sticker[i][2] = deepcopy(pi_degree)
    sticker[i][3] = deepcopy(reverse_deg)

for t in range(S):
    for c in range(4):
        