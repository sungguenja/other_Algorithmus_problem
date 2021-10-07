from copy import deepcopy
def findRoute(start_i,start_j,start_d,N,M,grid):
    visit = [[[False]*4 for j in range(2*M+1)] for i in range(2*N+1)]
    dist = 0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    i,j,d=start_i,start_j,start_d
    while not visit[i][j][d]:
        visit[i][j][d] = True
        ni = i + di[d]
        nj = j + dj[d]
        nd = d

        if not (0<=ni<2*N+1):
            ni = ni%(2*N+1)
        if not (0<=nj<2*M+1):
            nj = nj%(2*M+1)

        if ni & 1 and nj & 1:
            dist += 1
            now_dir = grid[ni//2][nj//2]
            if now_dir == 'L':
                nd = (d - 1) % 4
            elif now_dir == 'R':
                nd = (d + 1) % 4
            ni = ni + di[nd]
            nj = nj + dj[nd]
        i,j,d = ni,nj,nd
    return dist,visit

def solution(grid):
    answer = []

    N = len(grid)
    M = len(grid[0])
    visit = []
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for i in range(1,2*N+1,2):
        for j in range(1,2*M+1,2):
            for k in range(4):
                for check in range(len(visit)):
                    if visit[check][i+di[k]][j+dj[k]][k]:
                        break
                else:
                    dist,status = findRoute(i,j,k,N,M,grid)
                    answer.append(dist)
                    visit.append(deepcopy(status))

    return answer
