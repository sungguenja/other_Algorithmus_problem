from copy import deepcopy
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
    
    ans = check(room,N,M)
    if ans<last_cnt:
        last_cnt=ans
    
    for i in range(len(visit)):
        if visit[i] < len(direction[now_cc[i][2]]):
            visit[i] += 1
            case(N,M)
            visit[i] -= 1

def check(chamber,N,M):
    func_room = deepcopy(chamber)

    for v in range(len(visit)):
        i=now_cc[v][0]
        j=now_cc[v][1]
        for k in direction[now_cc[v][2]][visit[v]]:
            ni=i
            nj=j
            while 0<=ni<N and 0<=nj<M and func_room[ni][nj] != 6:
                func_room[ni][nj] = '#'
                ni+=see[k][0]
                nj+=see[k][1]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if func_room[i][j] == 0:
                cnt += 1

    return cnt

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