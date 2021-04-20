from collections import deque
def cleanRoom(N,H,W,start,room,dirty_list):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    result = (H+1)*(W+1)*(N+1)
    Que = deque()
    Que.append((start[0],start[1],'0'*N,0))
    visit = [[{} for j in range(W)] for i in range(H)]
    while Que:
        i,j,now,cnt = Que.popleft()
        if cnt > result:
            continue
        if now == '1'*N:
            if result > cnt:
                result = cnt
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<H and 0<=nj<W:
                if room[ni][nj] != 'x' and (visit[ni][nj].get(now) == None or visit[ni][nj].get(now) > cnt + 1):
                    if room[ni][nj] == '.' or room[ni][nj] == 'o':
                        visit[ni][nj][now] = cnt + 1
                        Que.append((ni,nj,now,cnt+1))
                    else:
                        visit[ni][nj][now] = cnt + 1
                        dirty_position = dirty_list.index((ni,nj))
                        next_bit = now[:dirty_position] + '1' + now[dirty_position+1:]
                        Que.append((ni,nj,next_bit,cnt+1))
    if result == (H+1)*(W+1)*(N+1):
        result = -1
    return result

while True:
    W,H = map(int,input().split())
    if W == 0 and H == 0:
        break
    N = 0
    room = [0]*H
    start = [0,0]
    dirty_list = []
    for i in range(H):
        horizon = list(input())
        for j in range(W):
            if horizon[j] == 'o':
                start = [i,j]
            elif horizon[j] == '*':
                N += 1
                dirty_list.append((i,j))
        room[i] = horizon[:]
    
    answer = cleanRoom(N,H,W,start,room,dirty_list)
    print(answer)