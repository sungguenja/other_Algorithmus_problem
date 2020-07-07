N,L = map(int,input().split())
runway = [list(map(int,input().split())) for i in range(N)]

cnt = 0
# 가로
for i in range(N):
    check = [False]*N
    j=0
    trigger = True
    while j<N-1:
        if runway[i][j] == runway[i][j+1]:
            j+=1
            continue

        if runway[i][j] - runway[i][j+1] == 1: # 내려가기
            bridge = j+L
            if bridge >= N:
                trigger = False
                break

            flag = False
            for k in range(j+1,bridge+1):
                check[k] = True
                if runway[i][j] - runway[i][k] != 1:
                    flag = True
                    break
            if flag:
                trigger = False
                break
            j = bridge
        elif runway[i][j] - runway[i][j+1] == -1: # 올라가기
            bridge = j - L
            if bridge + 1< 0:
                trigger = False
                break

            flag = False
            for k in range(bridge+1,j+1):
                if runway[i][j] != runway[i][k] or check[k]:
                    flag = True
                    break
                check[k] = True
            if flag:
                trigger = False
                break
            j+=1
        else: # 다 안되는 경우
            trigger = False
            break
    if trigger:
        cnt+=1

for i in range(N):
    for j in range(i,N):
        runway[i][j],runway[j][i] = runway[j][i],runway[i][j]

# 세로
for i in range(N):
    check = [False]*N
    j=0
    trigger = True
    while j<N-1:
        if runway[i][j] == runway[i][j+1]:
            j+=1
            continue

        if runway[i][j] - runway[i][j+1] == 1: # 내려가기
            bridge = j+L
            if bridge >= N:
                trigger = False
                break

            flag = False
            for k in range(j+1,bridge+1):
                check[k] = True
                if runway[i][j] - runway[i][k] != 1:
                    flag = True
                    break
            if flag:
                trigger = False
                break
            else:
                j = bridge
        elif runway[i][j] - runway[i][j+1] == -1: # 올라가기
            bridge = j - L
            if bridge+1 < 0:
                trigger = False
                break

            flag = False
            for k in range(bridge+1,j+1):
                if runway[i][j] != runway[i][k] or check[k]:
                    flag = True
                    break
                check[k] = True
            if flag:
                trigger = False
                break
            else:
                j+=1
        else: # 다 안되는 경우
            trigger = False
            break
    if trigger:
        cnt+=1

print(cnt)