for t in range(int(input())):
    M,N,K = map(int,input().split())

    field =[[0]*M for _ in range(N)]

    for _ in range(K):                  # 배추농사
        i,j=map(int,input().split())
        field[j][i] = 1

    bug = 0
    stack = []
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                stack.append([i,j])
                bug+=1
                field[i][j] == 'b'
                while stack != []:
                    X = stack.pop()
                    ni,nj=X[0],X[1]
                    for k in direction:
                        if N>ni+k[0]>=0 and M>nj+k[1]>=0:
                            if field[ni+k[0]][nj+k[1]] == 1:
                                stack.append([ni+k[0],nj+k[1]])
                                field[ni+k[0]][nj+k[1]] = 'b'
    print(bug)