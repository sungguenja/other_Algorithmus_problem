import queue
def bfs(start,end,size,now):
    que = queue.Queue()
    for i in range(size):
        if usado[now][i] != -1:
            que.put([i,[usado[now][i][0]]])
    while que.qsize()>=1:
        j,root = que.get()
        if usado[start][end] != -1 and len(root)>=usado[start][end][1]:
            continue
        if j == end:
            if usado[start][end] == -1:
                usado[start][end] = [min(root),len(root)]
                continue
            else:
                if usado[start][end][1] > len(root):
                    usado[start][end] = [min(root),len(root)]
                    continue
        for nj in range(size):
            if usado[j][nj] != -1 and usado[j][nj][1] == 0:
                que.put([nj,root+[usado[j][nj][0]]])


N,Q = map(int,input().split())
usado = [[-1]*N for i in range(N)]

for i in range(N-1):
    p,q,r = map(int,input().split())
    usado[p-1][q-1] = [r,0]
    usado[q-1][p-1] = [r,0]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if usado[i][j] == -1:
            visit = [[False]*N for _ in range(N)]
            bfs(i,j,N,i)

for _ in range(Q):
    k,v=map(int,input().split())
    cnt = 0
    for i in range(N):
        if usado[v-1][i] != -1:
            if type(usado[v-1][i]) == int:
                if usado[v-1][i]>=k:
                    cnt += 1
            elif type(usado[v-1][i]) == list:
                if usado[v-1][i][0]>=k:
                    cnt += 1
    print(cnt)