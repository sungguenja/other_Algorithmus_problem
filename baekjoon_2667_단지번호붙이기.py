N=int(input())
direction = [[0,1],[1,0],[0,-1],[-1,0]]    # 저에게 우상향 방향을 주시옵소서

danzi = []          # 단지
for _ in range(N):
    horizon = []
    horizon = list(input())
    danzi.append(horizon)

stack = []                          # 위치저장용
count_stack = []                    # 단지 크기 스택용
for i in range(N):
    for j in range(N):
        danzi_count = 0
        if danzi[i][j] == '1':      # 단지를 포착했다
            danzi[i][j] = 1
            danzi_count += 1
            stack.append([i,j])     # 단지 시작점 스택
            while stack != []:
                X = stack.pop()
                ni,nj = X[0], X[1]
                for k in direction:
                    if N>ni+k[0]>=0 and N>nj+k[1]>=0:
                        if danzi[ni+k[0]][nj+k[1]] == '1':
                            danzi[ni+k[0]][nj+k[1]] = 1
                            stack.append([ni+k[0],nj+k[1]])
                            danzi_count += 1
            count_stack.append(danzi_count)

print(len(count_stack))
count_stack.sort()
for k in count_stack:
    print(k)