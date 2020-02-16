direction = [[0,1],[1,0],[0,-1],[-1,0]]

N,M = map(int, input().split())
maze=[list(input()) for _ in range(N)]
visit_maze = [[[0]*M for _ in range(N)],[[0]*M for _ in range(N)]]

que = [[0,0,1]]
where_stack = []
root = N*M+1
while que != []:
    for z in visit_maze:
        print(z)
    print()
    X = que.pop(0)
    ni,nj,charge=X[0],X[1],X[2]
    if [ni,nj] == [N-1,M-1] and root>visit_maze[ni][nj]+1:
        root = visit_maze[ni][nj] + 1
    
    for k in range(4):
        if 0<=ni+direction[k][0]<N and 0<=nj+direction[k][1]<M :
            if maze[ni+direction[k][0]][nj+direction[k][1]] == '0':
                visit_maze[charge][ni+direction[k][0]][nj+direction[k][1]] = visit_maze[charge][ni][nj] + 1
                que.append([ni+direction[k][0],nj+direction[k][1],charge])
            if maze[ni+direction[k][0]][nj+direction[k][1]] == '1' and charge == 1:
                visit_maze[0][ni+direction[k][0]][nj+direction[k][1]] = visit_maze[charge][ni][nj] + 1
                que.append([ni+direction[k][0],nj+direction[k][1],charge-1])
if root == N*M+1:
    root = -1

print(root)