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
N=int(input())
cycle = list(map(str, input().split()))
for i in range(N):
    if cycle[i] == 'U+':
        cube[0][3],cube[1][3],cube[2][3],cube[2][4],cube[2][5],cube[1][5],cube[0][5],cube[0][4] = cube[1][3],cube[2][3],cube[2][4],cube[2][5],cube[1][5],cube[0][5],cube[0][4],cube[0][3]
        cube[3][:3], cube[3][3:6], cube[3][6:9], cube[11][3:6] = cube[11][3:6], cube[3][:3], cube[3][3:6], cube[3][6:9]
    elif cycle[i] == 'U-':
        cube[0][3],cube[0][4],cube[0][5],cube[1][5],cube[2][5],cube[2][4],cube[2][3],cube[1][3] = cube[1][3],cube[0][3],cube[0][4],cube[0][5],cube[1][5],cube[2][5],cube[2][4],cube[2][3]
        cube[3][:3], cube[3][3:6], cube[3][6:9], cube[11][3:6] = cube[3][3:6], cube[3][6:9], cube[11][3:6], cube[3][:3]
    elif cycle[i] == 'D+':
        cube[6][3],cube[6][4],cube[6][5],cube[7][5],cube[8][5],cube[8][4],cube[8][3],cube[7][3] = cube[7][3],cube[6][3],cube[6][4],cube[6][5],cube[7][5],cube[8][5],cube[8][4],cube[8][3]
        cube[5][:3], cube[5][3:6], cube[5][6:9], cube[9][3:6] = cube[9][3:6], cube[5][:3], cube[5][3:6], cube[5][6:9]
    elif cycle[i] == 'D-':
        cube[6][3],cube[7][3],cube[8][3],cube[8][4],cube[8][5],cube[7][5],cube[6][5],cube[6][4] = cube[6][4],cube[6][3],cube[7][3],cube[8][3],cube[8][4],cube[8][5],cube[7][5],cube[6][5]
    elif cycle[i] == 'F+':
        cube[3][3],cube[4][3],cube[5][3],cube[5][4],cube[5][5],cube[4][5],cube[3][5],cube[3][4] = cube[4][3],cube[5][3],cube[5][4],cube[5][5],cube[4][5],cube[3][5],cube[3][4],cube[3][3]
        cube[3][2],cube[2][3],cube[2][4],cube[2][5],cube[3][6],cube[3][7],cube[3][8],cube[6][5],cube[6][4],cube[6][3],cube[5][2],cube[4][2] = cube[4][2],cube[3][2],cube[2][3],cube[2][4],cube[2][5],cube[3][6],cube[3][7],cube[3][8],cube[6][5],cube[6][4],cube[6][3],cube[5][2]
    elif cycle[i] == 'F-':
        cube[3][3],
# for k in cube:
#     print(k)