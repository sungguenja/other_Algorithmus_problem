di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
nutriton = [[5]*N for _ in range(N)]
S2D2 = [list(map(int,input().split())) for _ in range(N)]
ground = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int,input().split())
    ground[x-1][y-1][z] = 1

for _ in range(K):
    # 봄 여름
    for i in range(N):
        for j in range(N):
            if ground[i][j]:
                tree = {}
                dead_tree = 0
                for now_age in sorted(ground[i][j].keys()):
                    if now_age*ground[i][j][now_age] <= nutriton[i][j]:
                        nutriton[i][j] -= now_age*ground[i][j][now_age]
                        tree[now_age+1] = ground[i][j][now_age]
                    else:
                        safe = nutriton[i][j]//now_age
                        if safe == 0:
                            dead_tree += (now_age//2)*ground[i][j][now_age]
                        else:
                            nutriton[i][j] -= now_age*safe
                            tree[now_age+1] = safe
                            dead_tree += (now_age//2)*(ground[i][j][now_age]-safe)
                nutriton[i][j] += dead_tree
                ground[i][j] = tree
    # 가을
    for i in range(N):
        for j in range(N):
            if ground[i][j]:
                for age in ground[i][j].keys():
                    if age%5==0:
                        num = ground[i][j][age]
                        for k in range(8):
                            ni=i+di[k]
                            nj=j+dj[k]
                            if 0<=ni<N and 0<=nj<N:
                                if 1 not in ground[ni][nj].keys():
                                    ground[ni][nj][1] = num
                                else:
                                    ground[ni][nj][1] += num
    # 겨울
    for i in range(N):
        for j in range(N):
            nutriton[i][j] += S2D2[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += sum(ground[i][j].values())
print(answer)