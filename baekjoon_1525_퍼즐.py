from collections import deque
from copy import deepcopy

def makePuzzleString(puzzle):
    tmp_key = ''
    for p in range(3):
        tmp_key = tmp_key + ''.join(puzzle[p])
    return tmp_key

start = [-1,-1]
puzzle = [list(map(str,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        if puzzle[i][j] == '0':
            start = [i,j]
            break
    if start[0] != -1 and start[1] != -1:
        break

di = [0,1,0,-1]
dj = [1,0,-1,0]
que = deque()
que.append([start[0],start[1],makePuzzleString(puzzle),0])

visit = {}
answer = -1
trigger = 0

while que:
    i,j,now_puzzle,cnt = que.popleft()
    tmp_puzzle = [[],[],[]]
    for ii in range(3):
        for jj in range(3):
            tmp_puzzle[ii].append(now_puzzle[3*ii+jj])

    if i == 2 and j == 2:
        if answer == -1 or cnt < answer:
            checker = 1
            
            for ii in range(3):
                for jj in range(3):
                    if tmp_puzzle[ii][jj] == str(checker):
                        checker += 1

            if checker == 9:
                answer = cnt
                continue

    if answer != -1 and cnt > answer:
        continue

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        
        if 0<=ni<3 and 0<=nj<3:
            now_key = ''
            for p in range(3):
                now_key = now_key + ''.join(tmp_puzzle[p])
            if visit.get(now_key) == None:
                visit[now_key] = [[-1]*3 for _ in range(3)]
            
            if visit[now_key][ni][nj] == -1:
                visit[now_key][ni][nj] = cnt + 1
                tmp_puzzle[ni][nj], tmp_puzzle[i][j] = tmp_puzzle[i][j], tmp_puzzle[ni][nj]
                que.append([ni,nj,makePuzzleString(tmp_puzzle),cnt+1])
                tmp_puzzle[ni][nj], tmp_puzzle[i][j] = tmp_puzzle[i][j], tmp_puzzle[ni][nj]

print(answer)