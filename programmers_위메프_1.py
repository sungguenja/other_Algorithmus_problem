dx = [0,1]
dy = [1,0]
def solution(N,M,guide):
    answer = [[-1]*M for i in range(N)]
    que = [[0,0]]
    answer[0][0] = guide[0][0]
    while que != []:
        i,j = que.pop(0)
        for k in range(2):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0<=ni<N and 0<=nj<M:
                if answer[ni][nj]<answer[i][j]+guide[ni][nj]:
                    answer[ni][nj] = answer[i][j]+guide[ni][nj]
                    que.append([ni,nj])
    return answer[-1][-1]