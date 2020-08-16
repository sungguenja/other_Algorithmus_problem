answer = -1
direction = [[0,1],[1,0],[0,-1],[-1,0]]

def solution(i,j,k):
    global answer
    count = 0
    ni = i
    nj = j
    while 0<=ni<N and 0<=nj<N and candy[i][j] == candy[ni][nj]:
        count += 1
        ni += direction[k][0]
        nj += direction[k][1]
    ni = i + direction[(k+2)%4][0]
    nj = j + direction[(k+2)%4][1]
    while 0<=ni<N and 0<=nj<N and candy[i][j] == candy[ni][nj]:
        count += 1
        ni += direction[(k+2)%4][0]
        nj += direction[(k+2)%4][1]
    if count>answer:
        answer = count

N=int(input())
candy = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + direction[k][0]
            nj = j + direction[k][1]
            if 0<=ni<N and 0<=nj<N:
                candy[i][j], candy[ni][nj] = candy[ni][nj], candy[i][j]
                for t in range(4):
                    solution(i,j,t)
                candy[i][j], candy[ni][nj] = candy[ni][nj], candy[i][j]
print(answer)