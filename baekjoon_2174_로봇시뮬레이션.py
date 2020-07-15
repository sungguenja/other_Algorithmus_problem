direction = [[-1,0],[0,1],[1,0],[0,-1]]
N,M = map(int,input().split())
A,B = map(int,input().split())

robots = [0]*A
commands = [0]*B
# 게임 맵
game = [[0]*N for i in range(M)]
# 로봇 입력 받기
for i in range(A):
    robots[i] = list(input().split())
    robots[i][0],robots[i][1] = robots[i][1],robots[i][0]
    robots[i][0] = M-int(robots[i][0])
    robots[i][1] = int(robots[i][1])-1
    if robots[i][2] == 'N':
        robots[i][2] = 0
    elif robots[i][2] == 'E':
        robots[i][2] = 1
    elif robots[i][2] == 'S':
        robots[i][2] = 2
    else:
        robots[i][2] = 3
    # 주어진 그림과 우리가 표현할 지도가 좀 다르다
    game[robots[i][0]][robots[i][1]] = str(i+1)

for i in range(B):
    commands[i] = list(input().split())
    commands[i][0] = int(commands[i][0])-1
    commands[i][2] = int(commands[i][2])

end = 'OK'
for com in commands:
    i,j,k=robots[com[0]]
    timer = com[2]
    if com[1] != 'F':
        timer = timer%4
    for t in range(timer):
        if com[1] == 'L':
            k = (k-1)%4
        elif com[1] == 'R':
            k = (k+1)%4
        elif com[1] == 'F':
            game[i][j] = 0
            i += direction[k][0]
            j += direction[k][1]
            if i<0 or i>=M or j<0 or j>=N:
                end = 'Robot {0} crashes into the wall'.format(com[0]+1)
                break
            elif game[i][j] != 0:
                end = 'Robot {0} crashes into robot {1}'.format(com[0]+1,game[i][j])
                break
            else:
                game[i][j] = str(com[0]+1)
    robots[com[0]] = [i,j,k]
    if end != 'OK':
        break

print(end)