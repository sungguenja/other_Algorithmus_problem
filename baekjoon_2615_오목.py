def checkOmok(omok,i,j,k):
    start = 0
    di = [1,1,0,-1,-1,-1,0,1]
    dj = [0,1,1,1,0,-1,-1,-1]
    reverse_direction = (k + 4) % 8
    nowOmok = omok[i][j]
    ni, nj = i,j
    while True:
        if omok[ni][nj] == nowOmok:
            start += 1
            ni += di[k]
            nj += dj[k]
        else:
            break

        if start >= 6 or ni < 0 or ni >= 19 or nj < 0 or nj >= 19:
            break
    
    if start == 5:
        ri,rj = i + di[reverse_direction], j + dj[reverse_direction]
        while True:
            if start >= 6 or ri < 0 or ri >= 19 or rj < 0 or rj >= 19:
                break

            if omok[ri][rj] == nowOmok:
                start += 1
                ri += di[reverse_direction]
                rj += dj[reverse_direction]
            else:
                break

    return start == 5


def solution(omok):
    void = '0'
    first = '1'
    second = '2'
    di = [1,1,0,-1]
    dj = [0,1,1,1]
    for i in range(19):
        for j in range(19):
            if omok[i][j] != void:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0<=ni<19 and 0<=nj<19 and omok[i][j] == omok[ni][nj] and checkOmok(omok,i,j,k):
                        return omok[i][j],i,j
    return '0'

board = [list(input().split()) for _ in range(19)]
answer = solution(board)
if answer == '0':
    print('0')
else:
    print(answer[0])
    print(answer[1]+1,answer[2]+1)