def dfs(start,N):
    global visit

    for i in range(N+1):
        if i not in visit and node[start][i] != 0:
            visit += [i]
            dfs(i,N)

N,M,start=map(int,input().split())
node=[[0]*(N+1)]
node.extend([[0]*(N+1) for _ in range(N)])
for _ in range(M):
    x,y=map(int,input().split())
    node[y][x]=1
    node[x][y]=1

bfs_line = [start]
que = [start]
bfs_visit = [0]*(N+1)
bfs_visit[start] = 1
while que != []:
    now = que.pop(0)
    for j in range(N+1):
        if node[now][j] != 0 and bfs_visit[j] == 0:
            que.append(j)
            bfs_line.append(j)
            bfs_visit[j] = 1
visit=[start]
dfs(start,N)
print(' '.join(map(str,visit)))
print(' '.join(map(str,bfs_line)))