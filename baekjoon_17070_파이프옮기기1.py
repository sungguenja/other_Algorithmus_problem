direction = [[0,1],[1,1],[1,0]]
N=int(input())
answer = 0
basement = [list(map(int,input().split())) for _ in range(N)]
Que = [0]*(2*N**3)
Que[0] = [0,1,'-']
l=-1
r=0
while r > l:
    l+=1
    now = Que[l]
    if type(now) == int:
        break
    i,j,shape = now[0],now[1],now[2]
    if i==N-1 and j==N-1:
        answer+=1
        continue
    for k in direction:
        if shape == '-' and k==[1,0]:
            continue
        elif shape == '|' and k==[0,1]:
            continue
        ni = i + k[0]
        nj = j + k[1]
        if 0<=ni<N and 0<=nj<N:
            if k==[1,1]:
                if basement[ni][nj] == 1 or (i+1<N and basement[i+1][j] == 1) or (j+1<N and basement[i][j+1]==1):
                    continue
                else:
                    r+=1
                    Que[r] = [ni,nj,'/']
            else:
                if basement[ni][nj] != 1:
                    if k==[1,0]:
                        r += 1
                        Que[r] = [ni,nj,'|']
                    else:
                        r += 1
                        Que[r] = [ni,nj,'-']

print(answer)