def solution(maze):
    answer = 0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    i = 0
    j = 0
    if maze[0][1] == 1:
        d = 1
    else:
        d = 0
    N=len(maze)
    while i!=N-1 or j!=N-1:
        left_i = i + di[d-1]
        left_j = j + dj[d-1]
        if 0<=left_i<N and 0<=left_j<N and maze[left_i][left_j] == 0:
            d = d-1
            if d == -1:
                d = 3
            i = i + di[d]
            j = j + dj[d]
            answer += 1
        else:
            ni = i + di[d]
            nj = j + dj[d]
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] == 0:
                i = ni
                j = nj
                answer += 1
            else:
                d = d+1
                if d==4:
                    d=0
    return answer
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))