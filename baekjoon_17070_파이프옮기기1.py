direction = [[0,1],[1,1],[1,0]]
N=int(input())
answer = 0
basement = [list(map(int,input().split())) for _ in range(N)]
Que = [[0,1,'-']]
while Que != []:
    now = Que.pop(0)
    i,j,shape = now[0],now[1],now[2]
    for k in direction:
        if k==[1,1] and ((0<=i+1<N and 0<=j+1<N and basement[i+1][j+1] == 1) or (0<=i+1<N and basement[i+1][j] == 1) or (0<=j+1<N and basement[i][j+1]==1)):
            continue
        ni = i+k[0]
        nj = j+k[1]
        if 0<=ni<N and 0<=nj<N:
            if ni==N-1 and nj==N-1:
                answer+=1
                continue
            elif shape=='-' and k==[1,0]:
                continue
            elif shape=='|' and k==[0,1]:
                continue
            elif basement[ni][nj] == 1:
                continue
            else:
                if ni-i==0 and nj-j==1:
                    Que.append([ni,nj,'-'])
                elif ni-i==1 and nj-j==1:
                    Que.append([ni,nj,'/'])
                elif ni-i==1 and nj-j==0:
                    Que.append([ni,nj,'|'])
print(answer)