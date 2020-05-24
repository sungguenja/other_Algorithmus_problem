def solution(m, n, puddles):
    road = [[0]*m for _ in range(n)]
    puddles = list(map(lambda x: [x[0]-1,x[1]-1],puddles))
    trigger = False
    for i in range(m):
        for j in puddles:
            if [0,i]==j:
                trigger = True
                break
        if trigger:
            break
        road[0][i] = 1
    
    trigger = False
    for i in range(n):
        for j in puddles:
            if [i,0]==j:
                trigger = True
                break
        if trigger:
            break
        road[i][0] = 1
    
    for i in range(1,n):
        for j in range(1,m):
            trigger = False
            for k in puddles:
                if [i,j] == k:
                    trigger = True
                    break
            if trigger:
                continue
            road[i][j] = road[i-1][j] + road[i][j-1]
    return road[n-1][m-1]%1000000007

print(solution(4,3,[[2,2]]))