from collections import deque
N,M = map(int,input().split())
lab = [0]*N
virus = []
for i in range(N):
    horizon = list(map(int,input().split()))
    for j in range(N):
        if horizon[j] == 2:
            virus.append([i,j])
    lab[i] = horizon[:]
answer = (N+1)**2
di = [0,1,0,-1]
dj = [1,0,-1,0]

def solution(start=-1,cnt=0,case=[]):
    global answer
    if cnt>=M:
        visit = [[0]*N for i in range(N)]
        Que = deque()
        last_t = 0
        for k in case:
            i,j = k
            Que.append([i,j,0])
        trigger = False
        while len(Que) > 0:
            i,j,t = Que.popleft()
            if t>last_t and lab[i][j] != 2:
                last_t = t
            if last_t>answer:
                trigger = True
                break
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N and visit[ni][nj] == 0 and lab[ni][nj] != 1:
                    visit[ni][nj] = t+1
                    Que.append([ni,nj,t+1])
        for i in range(N):
            for j in range(N):
                if visit[i][j] == 0 and lab[i][j] == 0:
                    trigger = True
                if trigger:
                    break
            if trigger:
                break
        if trigger:
            return
        else:
            if answer>last_t:
                answer = last_t
            return
    else:
        for k in range(start+1,len(virus)):
            solution(k,cnt+1,case+[virus[k]])
solution()
if answer == (N+1)**2:
    answer = -1

print(answer)