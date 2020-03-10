import copy
N,M=map(int,input().split())

room=[0]*N
brand = [1,2,3,4,5]
direction = {1:[[0],[1],[2],[3]],2:[[0,2],[1,3]],3:[[0,1],[1,2],[2,3],[3,0]],4:[[2,3,0],[3,0,1],[0,1,2],[1,2,3]],5:[[0,1,2,3]]}
see = [[0,1],[1,0],[0,-1],[-1,0]]
last_cnt = N*M

def case(N,M):
    global last_cnt
    for i in range(len(visit)):
        if visit[i] >= len(direction[now_cc[i][2]]):
            return
    
    c_room = copy.deepcopy(room)

    for v in range(len(visit)):
        for k in range(len(direction[now_cc[v][2]][visit[v]])):
            while 0<=ni<N and 0<=nj<M:
                ni = ni+see[direction[now_cc[v][2]][visit[v]][k]][0]
                nj = nj+see[direction[now_cc[v][2]][visit[v]][k]][1]
                if 0<=ni<N and 0<=nj<M:
                    if c_room[ni][nj] == 0:
                        c_room[ni][nj] = '#'
                    elif c_room[ni][nj] == 6:
                        break
    else:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if c_room[i][j] == 0:
                    cnt += 1
        else:
            if cnt<last_cnt:
                last_cnt = cnt
    
    for i in range(len(visit)):
        if visit[i] < len(direction[now_cc[i][2]]):
            visit[i] += 1
            case(N,M)
            visit[i] -= 1


now_cc = []
for i in range(N):
    cctv=[]
    cctv=list(map(int,input().split()))
    for j in range(M):
        if cctv[j] in brand:
            now_cc.append([i,j,cctv[j]])
    room[i] = cctv
visit = [0]*len(now_cc)
case(N,M)
print(last_cnt)