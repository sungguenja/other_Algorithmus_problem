for _ in range(int(input())):
    N=int(input())
    cycle = list(map(str, input().split()))
    cube = [
            ['x','x','x','w','w','w','x','x','x'],
            ['x','x','x','w','w','w','x','x','x'],
            ['x','x','x','w','w','w','x','x','x'],
            ['g','g','g','r','r','r','b','b','b'],
            ['g','g','g','r','r','r','b','b','b'],
            ['g','g','g','r','r','r','b','b','b'],
            ['x','x','x','y','y','y','x','x','x'],
            ['x','x','x','y','y','y','x','x','x'],
            ['x','x','x','y','y','y','x','x','x'],
            ['x','x','x','o','o','o','x','x','x'],
            ['x','x','x','o','o','o','x','x','x'],
            ['x','x','x','o','o','o','x','x','x']
        ]
    for i in range(N):
        if cycle[i] == 'U+':
            cube[0][3],cube[0][4],cube[0][5],cube[1][5],cube[2][5],cube[2][4],cube[2][3],cube[1][3] = cube[2][3],cube[1][3],cube[0][3],cube[0][4],cube[0][5],cube[1][5],cube[2][5],cube[2][4]
            cube[11][3],cube[11][4],cube[11][5],cube[3][8],cube[3][7],cube[3][6],cube[3][5],cube[3][4],cube[3][3],cube[3][2],cube[3][1],cube[3][0] = cube[3][2],cube[3][1],cube[3][0],cube[11][3],cube[11][4],cube[11][5],cube[3][8],cube[3][7],cube[3][6],cube[3][5],cube[3][4],cube[3][3]
        elif cycle[i] == 'U-':
            cube[0][3],cube[0][4],cube[0][5],cube[1][5],cube[2][5],cube[2][4],cube[2][3],cube[1][3] = cube[0][5],cube[1][5],cube[2][5],cube[2][4],cube[2][3],cube[1][3],cube[0][3],cube[0][4]
            cube[11][3],cube[11][4],cube[11][5],cube[3][8],cube[3][7],cube[3][6],cube[3][5],cube[3][4],cube[3][3],cube[3][2],cube[3][1],cube[3][0] = cube[3][8],cube[3][7],cube[3][6],cube[3][5],cube[3][4],cube[3][3],cube[3][2],cube[3][1],cube[3][0],cube[11][3],cube[11][4],cube[11][5]
        elif cycle[i] == 'D+':
            cube[6][3],cube[6][4],cube[6][5],cube[7][5],cube[8][5],cube[8][4],cube[8][3],cube[7][3] = cube[8][3],cube[7][3],cube[6][3],cube[6][4],cube[6][5],cube[7][5],cube[8][5],cube[8][4]
            cube[5][3],cube[5][4],cube[5][5],cube[5][6],cube[5][7],cube[5][8],cube[9][5],cube[9][4],cube[9][3],cube[5][0],cube[5][1],cube[5][2] =  cube[5][0],cube[5][1],cube[5][2],cube[5][3],cube[5][4],cube[5][5],cube[5][6],cube[5][7],cube[5][8],cube[9][5],cube[9][4],cube[9][3]
        elif cycle[i] == 'D-':
            cube[6][3],cube[6][4],cube[6][5],cube[7][5],cube[8][5],cube[8][4],cube[8][3],cube[7][3] = cube[6][5],cube[7][5],cube[8][5],cube[8][4],cube[8][3],cube[7][3],cube[6][3],cube[6][4]
            cube[5][3],cube[5][4],cube[5][5],cube[5][6],cube[5][7],cube[5][8],cube[9][5],cube[9][4],cube[9][3],cube[5][0],cube[5][1],cube[5][2] = cube[5][6],cube[5][7],cube[5][8],cube[9][5],cube[9][4],cube[9][3],cube[5][0],cube[5][1],cube[5][2],cube[5][3],cube[5][4],cube[5][5]
        elif cycle[i] == 'F+':
            cube[3][3],cube[3][4],cube[3][5],cube[4][5],cube[5][5],cube[5][4],cube[5][3],cube[4][3] = cube[5][3],cube[4][3],cube[3][3],cube[3][4],cube[3][5],cube[4][5],cube[5][5],cube[5][4]
            cube[2][3],cube[2][4],cube[2][5],cube[3][6],cube[4][6],cube[5][6],cube[6][5],cube[6][4],cube[6][3],cube[5][2],cube[4][2],cube[3][2] = cube[5][2],cube[4][2],cube[3][2],cube[2][3],cube[2][4],cube[2][5],cube[3][6],cube[4][6],cube[5][6],cube[6][5],cube[6][4],cube[6][3]
        elif cycle[i] == 'F-':
            cube[3][3],cube[3][4],cube[3][5],cube[4][5],cube[5][5],cube[5][4],cube[5][3],cube[4][3] = cube[3][5],cube[4][5],cube[5][5],cube[5][4],cube[5][3],cube[4][3],cube[3][3],cube[3][4]
            cube[2][3],cube[2][4],cube[2][5],cube[3][6],cube[4][6],cube[5][6],cube[6][5],cube[6][4],cube[6][3],cube[5][2],cube[4][2],cube[3][2] = cube[3][6],cube[4][6],cube[5][6],cube[6][5],cube[6][4],cube[6][3],cube[5][2],cube[4][2],cube[3][2],cube[2][3],cube[2][4],cube[2][5]
        elif cycle[i] == 'L+':
            cube[3][0],cube[3][1],cube[3][2],cube[4][2],cube[5][2],cube[5][1],cube[5][0],cube[4][0] = cube[5][0],cube[4][0],cube[3][0],cube[3][1],cube[3][2],cube[4][2],cube[5][2],cube[5][1]
            cube[0][3],cube[1][3],cube[2][3],cube[3][3],cube[4][3],cube[5][3],cube[6][3],cube[7][3],cube[8][3],cube[9][3],cube[10][3],cube[11][3] = cube[9][3],cube[10][3],cube[11][3],cube[0][3],cube[1][3],cube[2][3],cube[3][3],cube[4][3],cube[5][3],cube[6][3],cube[7][3],cube[8][3]
        elif cycle[i] == 'L-':
            cube[3][0],cube[3][1],cube[3][2],cube[4][2],cube[5][2],cube[5][1],cube[5][0],cube[4][0] = cube[3][2],cube[4][2],cube[5][2],cube[5][1],cube[5][0],cube[4][0],cube[3][0],cube[3][1]
            cube[0][3],cube[1][3],cube[2][3],cube[3][3],cube[4][3],cube[5][3],cube[6][3],cube[7][3],cube[8][3],cube[9][3],cube[10][3],cube[11][3] = cube[3][3],cube[4][3],cube[5][3],cube[6][3],cube[7][3],cube[8][3],cube[9][3],cube[10][3],cube[11][3],cube[0][3],cube[1][3],cube[2][3]
        elif cycle[i] == 'R+':
            cube[3][6],cube[3][7],cube[3][8],cube[4][8],cube[5][8],cube[5][7],cube[5][6],cube[4][6] = cube[5][6],cube[4][6],cube[3][6],cube[3][7],cube[3][8],cube[4][8],cube[5][8],cube[5][7]
            cube[2][5],cube[1][5],cube[0][5],cube[11][5],cube[10][5],cube[9][5],cube[8][5],cube[7][5],cube[6][5],cube[5][5],cube[4][5],cube[3][5] = cube[5][5],cube[4][5],cube[3][5],cube[2][5],cube[1][5],cube[0][5],cube[11][5],cube[10][5],cube[9][5],cube[8][5],cube[7][5],cube[6][5]
        elif cycle[i] == 'R-':
            cube[3][6],cube[3][7],cube[3][8],cube[4][8],cube[5][8],cube[5][7],cube[5][6],cube[4][6] = cube[3][8],cube[4][8],cube[5][8],cube[5][7],cube[5][6],cube[4][6],cube[3][6],cube[3][7]
            cube[2][5],cube[1][5],cube[0][5],cube[11][5],cube[10][5],cube[9][5],cube[8][5],cube[7][5],cube[6][5],cube[5][5],cube[4][5],cube[3][5] = cube[11][5],cube[10][5],cube[9][5],cube[8][5],cube[7][5],cube[6][5],cube[5][5],cube[4][5],cube[3][5],cube[2][5],cube[1][5],cube[0][5]
        elif cycle[i] == 'B+':
            cube[11][5],cube[11][4],cube[11][3],cube[10][3],cube[9][3],cube[9][4],cube[9][5],cube[10][5] = cube[9][5],cube[10][5],cube[11][5],cube[11][4],cube[11][3],cube[10][3],cube[9][3],cube[9][4]
            cube[0][5],cube[0][4],cube[0][3],cube[3][0],cube[4][0],cube[5][0],cube[8][3],cube[8][4],cube[8][5],cube[5][8],cube[4][8],cube[3][8] = cube[5][8],cube[4][8],cube[3][8],cube[0][5],cube[0][4],cube[0][3],cube[3][0],cube[4][0],cube[5][0],cube[8][3],cube[8][4],cube[8][5]
        elif cycle[i] == 'B-':
            cube[11][5],cube[11][4],cube[11][3],cube[10][3],cube[9][3],cube[9][4],cube[9][5],cube[10][5] = cube[11][3],cube[10][3],cube[9][3],cube[9][4],cube[9][5],cube[10][5],cube[11][5],cube[11][4]
            cube[0][5],cube[0][4],cube[0][3],cube[3][0],cube[4][0],cube[5][0],cube[8][3],cube[8][4],cube[8][5],cube[5][8],cube[4][8],cube[3][8] = cube[3][0],cube[4][0],cube[5][0],cube[8][3],cube[8][4],cube[8][5],cube[5][8],cube[4][8],cube[3][8],cube[0][5],cube[0][4],cube[0][3]
    for k in range(3):
        print(''.join(cube[k][3:6]))