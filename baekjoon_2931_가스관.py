di = [0,1,0,-1]
dj = [1,0,-1,0]
H,W = map(int,input().split())
start = -1
end = -1
pipe = [0]*H
for i in range(H):
    horizon = list(input())
    if start == -1 or end == -1:
        for j in range(W):
            if horizon[j] == 'M':
                start = [i,j]
            if horizon[j] == 'Z':
                end = [i,j]
    pipe[i] = horizon[:]

direction = -1
first_step = []
for k in range(4):
    ni = start[0] + di[k]
    nj = start[1] + dj[k]
    if 0<=ni<H and 0<=nj<W:
        if k == 0 and (pipe[ni][nj] == '-' or pipe[ni][nj] == '+' or pipe[ni][nj] == '3' or pipe[ni][nj] == '4'):
            first_step = [ni,nj]
            direction = k
            break
        if k == 1 and (pipe[ni][nj] == '|' or pipe[ni][nj] == '+' or pipe[ni][nj] == '2' or pipe[ni][nj] == '3'):
            first_step = [ni,nj]
            direction = k
            break
        if k == 2 and (pipe[ni][nj] == '-' or pipe[ni][nj] == '+' or pipe[ni][nj] == '1' or pipe[ni][nj] == '2'):
            first_step = [ni,nj]
            direction = k
            break
        if k == 3 and (pipe[ni][nj] == '|' or pipe[ni][nj] == '+' or pipe[ni][nj] == '1' or pipe[ni][nj] == '4'):
            first_step = [ni,nj]
            direction = k
            break
