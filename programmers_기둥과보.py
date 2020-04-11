from copy import deepcopy
def check(architect,x,y,case,n):
    c_blue = deepcopy(architect)
    if case == 0:
        c_blue[y][x] = '0' + c_blue[y][x][1] + c_blue[y][x][2] + c_blue[y][x][3]
        c_blue[y+1][x] = c_blue[y+1][x][0] + '0' + c_blue[y+1][x][2] + c_blue[y+1][x][3]
    elif case == 1:
        c_blue[y][x] = c_blue[y][x][0] + c_blue[y][x][1] + '0' + c_blue[y][x][3]
        c_blue[y][x+1] = c_blue[y][x+1][0] + c_blue[y][x+1][1] + c_blue[y][x+1][2] + '0'
    for i in range(n+1):
        for j in range(n+1):
            if c_blue[i][j] != '0000':
                if c_blue[i][j][0] == '1':
                    if i==0 or (i>0 and c_blue[i][j][1]=='1') or c_blue[i][j][2] == '1' or c_blue[i][j][3] == '1':
                        continue
                    else:
                        return False, c_blue
                if c_blue[i][j][2] == '1':
                    if c_blue[i][j][1] == '1' or c_blue[i][j+1][1] == '1' or (c_blue[i][j][3] == '1' and c_blue[i][j+1][2] == '1'):
                        continue
                    else:
                        return False, c_blue
    return True, c_blue

def solution(n, build_frame):
    answer = []
    build = [['0000']*(n+1) for _ in range(n+1)]
    for i in range(len(build_frame)):
        command = build_frame[i]
        x,y,a,b = command[0], command[1], command[2], command[3]
        if b==1:
            if a==0:
                if y==0 or (y>0 and build[y][x][1]=='1') or build[y][x][2]=='1' or build[y][x][3] == '1':
                    build[y][x] = '1'+build[y][x][1] + build[y][x][2] + build[y][x][3]
                    build[y+1][x] = build[y+1][x][0] + '1' + build[y+1][x][2] + build[y+1][x][3]
            elif a==1:
                if build[y][x][1] == '1' or build[y][x+1][1] == '1' or (build[y][x][3] == '1' and build[y][x+1][2] == '1'):
                    build[y][x] = build[y][x][0] + build[y][x][1] + '1' + build[y][x][3]
                    build[y][x+1] = build[y][x+1][0] + build[y][x+1][1] + build[y][x+1][2] + '1'
        elif b==0:
            trigger, blue = check(build,x,y,a,n)
            if trigger:
                build = deepcopy(blue)
    for j in range(n+1):
        for i in range(n+1):
            if build[i][j][0] == '1':
                answer.append([j,i,0])
            if build[i][j][2] == '1':
                answer.append([j,i,1])
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))