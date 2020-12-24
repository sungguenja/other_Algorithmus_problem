from copy import deepcopy
R,C,M = map(int,input().split())
fishes = [0]*M
aqua = [[0]*C for i in range(R)]
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    aqua[r-1][c-1] = [r,c,s,d,z,i]
    fishes[i] = [r,c,s,d,z,i]
answer = 0
# 낚시왕 이동
for fisher in range(C):
    print('--------')
    for k in aqua:
        print(k)
    if M == 0: # 다잡힘
        break
    for i in range(R):
        if aqua[i][fisher] != 0:
            answer += aqua[i][fisher][-2]
            M -= 1
            fishes[aqua[i][fisher][-1]] = 0
            aqua[i][fisher] = 0
            break
    if M == 0:
        break
    after_fishing = [[0]*C for i in range(R)]
    for fish in fishes:
        if fish == 0:
            continue
        i,j,s,d,z,whe = fish
        if d==1:
            ni = i - s
            if ni<=0:
                ni = -1*ni
            nj = j
            if R != 1:
                checkpoint = ni//(R-1)
                ni = ni%(R-1)
                if checkpoint%2==1:
                    d=2
        elif d==2:
            ni = i + s
            nj = j
            if R != 1:
                checkpoint = ni//(R-1)
                ni = ni%(R-1)
                if checkpoint%2==1:
                    d=1
        elif d==3:
            nj = j + s
            ni = i
            if C != 1:
                checkpoint = nj//(C-1)
                nj = nj%(C-1)
                if checkpoint%2==1:
                    d=4
        elif d==4:
            nj = j - s
            if nj<=0:
                nj *= -1
            ni = i
            if C != 1:
                checkpoint = nj//(C-1)
                nj = nj%(C-1)
                if checkpoint%2==1:
                    d=3
        # 도착 포인트 상황
        if after_fishing[ni-1][nj-1] == 0:
            after_fishing[ni-1][nj-1] = [ni,nj,s,d,z,whe]
        else:
            if after_fishing[ni-1][nj-1][4] > z:
                fishes[whe] = 0
                M -= 1
            else:
                fishes[after_fishing[ni-1][nj-1][5]] = 0
                M -= 1
                after_fishing[ni-1][nj-1] = [ni,nj,s,d,z,whe]
    aqua = deepcopy(after_fishing)
    print('--------')
    for k in aqua:
        print(k)
print(answer)