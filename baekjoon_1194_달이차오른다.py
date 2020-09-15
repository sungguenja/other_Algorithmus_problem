from collections import deque
# 방향
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 입력값받기
N,M=map(int,input().split())
maze = [0]*N
minsik = []
for i in range(N):
    horizon = list(input())
    for j in range(M):
        if minsik != []:
            break
        if horizon[j] == '0':
            minsik = [i,j]
            break
    maze[i] = horizon[:]
# 가능한 열쇠의 경우의 수
key_case = {'000000':0,
'100000':0,'010000':0,'001000':0,'000100':0,'000010':0,'000001':0,
'110000':0,'101000':0,'100100':0,'100010':0,'100001':0,'011000':0,
'010100':0,'010010':0,'010001':0,'001100':0,'001010':0,'001001':0,
'000110':0,'000101':0,'000011':0,
'111000':0,'110100':0,'110010':0,'110001':0,'101100':0,'101010':0,'101001':0,'100110':0,'100101':0,'100011':0,'011100':0,'011010':0,'011001':0,'010110':0,'010101':0,'010011':0,'001110':0,'001101':0,'001011':0,'000111':0,
'111100':0,'111010':0,'111001':0,'110110':0,'110101':0,'110011':0,'101110':0,'101101':0,'101011':0,'100111':0,'011110':0,'011101':0,'011011':0,'010111':0,'001111':0,
'111110':0,'111101':0,'111011':0,'110111':0,'101111':0,'011111':0,
'111111':0}
visit = [[key_case.copy() for i in range(M)] for j in range(N)]
Que = deque([[minsik[0],minsik[1],'000000',0]])
visit[minsik[0]][minsik[1]]['000000'] = 1
answer = (N*M)**2
while len(Que) != 0:
    i,j,key,cnt=Que.popleft()
    if cnt>=answer:
        continue
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M and maze[ni][nj] != '#' and visit[ni][nj][key] == 0:
            visit[ni][nj][key] = 1
            if maze[ni][nj] == '.' or maze[ni][nj] == '0':
                Que.append([ni,nj,key,cnt+1])
            elif maze[ni][nj] == '1':
                if cnt+1<answer:
                    answer = cnt+1
            elif maze[ni][nj].islower():
                Que.append([ni,nj,key[:ord(maze[ni][nj])-97]+'1'+key[ord(maze[ni][nj])-96:],cnt+1])
            elif maze[ni][nj].isupper():
                if key[ord(maze[ni][nj])-65] == '1':
                    Que.append([ni,nj,key,cnt+1])
if answer == (N*M)**2:
    answer = -1
print(answer)