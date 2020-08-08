from copy import deepcopy
R,C,M = map(int,input().split())
fishing = [[0]*C for _ in range(R)]
fishes = []
for _ in range(M):
    i,j,s,d,z = map(int,input().split())
    if d == 1 or d == 2:
        s = s%((R-1)*2)
    if d == 3 or d == 4:
        s = s%((C-1)*2)
    fishing[i-1][j-1] = [_,z]
    fishes.append([s,d,z,i-1,j-1])

answer = 0
# 한칸씩 이동하니까
for fisher in range(C):
    if M==0:    # 끝나는 상황
        break

    # 찌 내려간다
    for j in range(R):
        if fishing[j][fisher] != 0:
            answer += fishing[j][fisher][1]
            fishes[fishing[j][fisher][0]] = 0
            fishing[j][fisher] = 0
            M-=1
            break

    # 상어 이동시키기
    after_fishing = [[0]*C for _ in range(R)]
    for fish in range(len(fishes)):
        if fishes[fish] == 0:
            continue
        speed,direction,size,i,j=fishes[fish]
        if direction == 1:  # 위
            ni = i - speed
            nj = j
            while ni<0 or ni>=R:
                if ni<0:
                    ni *= (-1)
                    direction = 2
                elif ni>=R:
                    ni = 2*R-2-ni
                    direction = 1
        elif direction == 2:    # 아래
            ni = i + speed
            nj = j
            while ni<0 or ni>=R:
                if ni<0:
                    ni *= (-1)
                    direction = 2
                elif ni>=R:
                    ni = 2*R-2-ni
                    direction = 1
        elif direction == 3:    # 오른쪽
            ni = i
            nj = j + speed
            while nj<0 or nj>=C:
                if nj<0:
                    nj *= (-1)
                    direction = 3
                elif nj>=C:
                    nj = 2*C-2-nj
                    direction = 4
        elif direction == 4:    # 왼쪽
            ni = i
            nj = j - speed
            while nj<0 or nj>=C:
                if nj<0:
                    nj *= (-1)
                    direction = 3
                elif nj>=C:
                    nj = 2*C-2-nj
                    direction = 4
        
        # 도착후
        fishes[fish] = [speed,direction,size,ni,nj]
        if after_fishing[ni][nj] == 0:
            after_fishing[ni][nj] = [fish,size]
        else:
            if after_fishing[ni][nj][1]>size:
                fishes[fish] = 0
                M-=1
            else:
                fishes[after_fishing[ni][nj][0]] = 0
                M-=1
                after_fishing[ni][nj] = [fish,size]
    fishing = deepcopy(after_fishing)
print(answer)