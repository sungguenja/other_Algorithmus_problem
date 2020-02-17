direction = [[0,1],[1,0],[0,-1],[-1,0]]

N,M = map(int, input().split())
maze=[list(input()) for _ in range(N)]
visit_maze = [[[N*M+1]*M for _ in range(N)],[[N*M+1]*M for _ in range(N)]]
visit_maze[0][0][0],visit_maze[1][0][0] = 1,1
que = [[0,0,1]]
where_stack = []
root = N*M+1
while que != []:
    X = que.pop(0)
    ni,nj,charge=X[0],X[1],X[2]
    if [ni,nj] == [N-1,M-1] and root>visit_maze[charge][ni][nj]:
        root = visit_maze[charge][ni][nj]
    
    for k in range(4):
        if 0<=ni+direction[k][0]<N and 0<=nj+direction[k][1]<M :
            if maze[ni+direction[k][0]][nj+direction[k][1]] == '0' and visit_maze[charge][ni][nj]+1<visit_maze[charge][ni+direction[k][0]][nj+direction[k][1]]:
                visit_maze[charge][ni+direction[k][0]][nj+direction[k][1]] = visit_maze[charge][ni][nj] + 1
                que.append([ni+direction[k][0],nj+direction[k][1],charge])
            if maze[ni+direction[k][0]][nj+direction[k][1]] == '1' and charge == 1 and visit_maze[charge][ni][nj]+1<visit_maze[0][ni+direction[k][0]][nj+direction[k][1]]:
                visit_maze[0][ni+direction[k][0]][nj+direction[k][1]] = visit_maze[charge][ni][nj] + 1
                que.append([ni+direction[k][0],nj+direction[k][1],charge-1])
if root == N*M+1:
    root = -1

print(root)