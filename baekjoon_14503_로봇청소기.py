direction = [[-1,0],[0,1],[1,0],[0,-1]]  # 북, 동, 남, 서 순서로

N,M=map(int,input().split())

R,C,D = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]           # 청소 상황
stack = [[R,C,D,0]]
clean_room = 0      # 청소하고 시작하니까 카운트 1부터

while stack != []:  # 위에부터 건져내자
    now = stack.pop()
    ni,nj,d,s = now[0], now[1], now[2], now[3]
    if s == 0:
        visit[ni][nj] = 1
        clean_room += 1
    for k in range(d-1,d-5,-1):    # 왼쪽 부터니까 이렇게 해두면 왼쪽 방향 가능
        if room[ni+direction[k%4][0]][nj+direction[k%4][1]] == 0 and visit[ni+direction[k%4][0]][nj+direction[k%4][1]] == 0: # 벽이 아니고 청소안했을시 그리고 혹시 4를 넘어가면 4로 나눴을 때 나머지로 하면 된다
            stack.append([ni+direction[k%4][0],nj+direction[k%4][1],k%4,0])
            break
    else:
        if room[ni+direction[(d+2)%4][0]][nj+direction[(d+2)%4][1]] != 1:
            stack.append([ni+direction[(d+2)%4][0],nj+direction[(d+2)%4][1],d,1])

print(clean_room)