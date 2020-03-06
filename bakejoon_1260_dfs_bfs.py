def dfs(start,N,visit=[]):
    global dfs_line
    visit+=[start]

    for i in range(N+1):
        if i not in visit and node[start][i] != 0:
            if i not in dfs_line:
                dfs_line.append(i)
            dfs(i,N,visit+[i])

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

dfs_line=[start]
dfs(start,N)
print(' '.join(map(str,dfs_line)))
print(' '.join(map(str,bfs_line)))