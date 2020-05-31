def solution(dirs):
    answer = 0
    visit = [['0000']*11 for _ in range(11)]
    i,j=5,5
    for _ in range(len(dirs)):
        direction = dirs[_]
        if direction == 'U':
            ni = i+1
            nj = j
        elif direction == 'D':
            ni = i-1
            nj = j
        elif direction == 'R':
            ni = i
            nj = j+1
        elif direction == 'L':
            ni = i
            nj = j-1
        if 0<=ni<11 and 0<=nj<11:
            if direction == 'U':
                if visit[i][j][0] == '0' and visit[ni][nj][1] == '0':
                    answer += 1
                visit[i][j] = '1' + visit[i][j][1] + visit[i][j][2] + visit[i][j][3]
                visit[ni][nj] = visit[ni][nj][0] + '1' + visit[ni][nj][2] + visit[ni][nj][3]
                i,j=ni,nj
            elif direction == 'D':
                if visit[i][j][1] == '0' and visit[ni][nj][0] == '0':
                    answer += 1
                visit[i][j] = visit[i][j][0] + '1' + visit[i][j][2] + visit[i][j][3]
                visit[ni][nj] = '1' + visit[ni][nj][1] + visit[ni][nj][2] + visit[ni][nj][3]
                i,j=ni,nj
            elif direction == 'L':
                if visit[i][j][2] == '0' and visit[ni][nj][3] == '0':
                    answer += 1
                visit[i][j] = visit[i][j][0] + visit[i][j][1] + '1' + visit[i][j][3]
                visit[ni][nj] = visit[ni][nj][0] + visit[ni][nj][1] + visit[ni][nj][2] + '1'
                i,j=ni,nj
            elif direction == 'R':
                if visit[i][j][3] == '0' and visit[ni][nj][2] == '0':
                    answer += 1
                visit[i][j] = visit[i][j][0] + visit[i][j][1] + visit[i][j][2] + '1'
                visit[ni][nj] = visit[ni][nj][0] + visit[ni][nj][1] + '1' + visit[ni][nj][3]
                i,j=ni,nj

    return answer

print(solution('ULURRDLLU'))