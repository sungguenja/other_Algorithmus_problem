from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]

def prisonBreak(person,H,W):
    Que = deque()
    Que.append((person[0],person[1],0))
    visit = [[-1]*W for i in range(H)]
    visit[person[0]][person[1]] = 0
    while Que:
        i,j,cnt = Que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<H and 0<=nj<W and visit[ni][nj] == -1:
                if prison[ni][nj] == '#':
                    visit[ni][nj] = cnt + 1
                    Que.append((ni,nj,cnt+1))
                elif prison[ni][nj] == '.' or prison[ni][nj] == '$':
                    visit[ni][nj] = cnt
                    Que.appendleft((ni,nj,cnt))
    
    return visit

N = int(input())
for t in range(N):
    H,W = map(int,input().split())
    prison = [list('.'*(W+2))]
    person = []
    answer = (H+1)*(W+1)*2
    for i in range(H):
        horizon = ['.'] + list(input()) + ['.']
        for j in range(W+2):
            if horizon[j] == "$":
               person.append((i+1,j)) 
        prison.append(horizon[:])
    
    prison.append(list('.'*(W+2)))

    first = prisonBreak(person[0],H+2,W+2)
    second = prisonBreak(person[1],H+2,W+2)
    third = prisonBreak((0,0),H+2,W+2)

    for i in range(H+2):
        for j in range(W+2):
            now = first[i][j] + second[i][j] + third[i][j]

            if prison[i][j] == '*' or first[i][j] == -1 or second[i][j] == -1 or third[i][j] == -1:
                continue
            
            if prison[i][j] == '#':
                now -= 2
            
            answer = min(answer,now)
    
    print(answer)