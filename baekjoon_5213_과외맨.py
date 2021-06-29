from collections import deque
from sys import stdin
input = stdin.readline
trigger = True
cnt = 0
N = int(input())

temple = []
horizon = [-1]*(2*N)
number = []
number_horizon = [-1]*(2*N)
for i in range(N*N - N//2):
    if N == 1:
        break
    ar = list(map(int,input().split()))
    if trigger:
        horizon[cnt*2] = ar[0]
        horizon[cnt*2 + 1] = ar[1]
        number_horizon[cnt*2] = i + 1
        number_horizon[cnt*2 + 1] = i + 1
    else:
        horizon[cnt*2 + 1] = ar[0]
        horizon[cnt*2 + 2] = ar[1]
        number_horizon[cnt*2 + 1] = i + 1
        number_horizon[cnt*2 + 2] = i + 1
    cnt += 1
    if trigger and cnt == N:
        temple.append(horizon)
        number.append(number_horizon)
        horizon = [-1]*(2*N)
        number_horizon = [-1]*(2*N)
        cnt = 0
        trigger = False
    elif not trigger and cnt == N - 1:
        temple.append(horizon)
        number.append(number_horizon)
        horizon = [-1]*(2*N)
        number_horizon = [-1]*(2*N)
        cnt = 0
        trigger = True

visit = [[[-1]*(2) for j in range(2*N)] for i in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

Que = deque()
Que.append((0,0,1,['1']))
answer = (N+1)**2
answer_list = []
while Que:
    i,j,cnt,route = Que.popleft()

    if cnt >= answer:
        continue
    
    if route[-1] == str(N*N - N//2):
        if cnt < answer:
            answer = cnt
            answer_list = route
        continue
    else:
        if answer_list == [] or int(answer_list[-1]) < int(route[-1]):
            answer_list = route

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<2*N:
            if number[ni][nj] == number[i][j] and (visit[ni][nj][0] == -1 or visit[ni][nj][0] > cnt):
                visit[ni][nj][0] = cnt
                Que.append((ni,nj,cnt,route))
                if ni % 2 == 0:
                    if nj % 2 == 0:
                        visit[ni][nj+1][0] = cnt
                        Que.append((ni,nj+1,cnt,route))
                    else:
                        visit[ni][nj-1][0] = cnt
                        Que.append((ni,nj-1,cnt,route))
                else:
                    if nj % 2 == 0:
                        visit[ni][nj-1][0] = cnt
                        Que.append((ni,nj-1,cnt,route))
                    else:
                        visit[ni][nj+1][0] = cnt
                        Que.append((ni,nj+1,cnt,route))
            else:
                if temple[ni][nj] == temple[i][j] and (visit[ni][nj][1] == -1 or visit[ni][nj][1] > cnt + 1):
                    visit[ni][nj][1] = cnt + 1
                    Que.append((ni,nj,cnt+1,route+[str(number[ni][nj])]))
                    if ni % 2 == 0:
                        if nj % 2 == 0:
                            visit[ni][nj+1][0] = cnt
                            Que.append((ni,nj+1,cnt+1,route+[str(number[ni][nj])]))
                        else:
                            visit[ni][nj-1][0] = cnt
                            Que.append((ni,nj-1,cnt+1,route+[str(number[ni][nj])]))
                    else:
                        if nj % 2 == 0:
                            visit[ni][nj-1][0] = cnt
                            Que.append((ni,nj-1,cnt+1,route+[str(number[ni][nj])]))
                        else:
                            visit[ni][nj+1][0] = cnt
                            Que.append((ni,nj+1,cnt+1,route+[str(number[ni][nj])]))
if answer == (N+1)**2 and answer_list != []:
    answer = len(answer_list)
print(answer)
print(' '.join(answer_list))