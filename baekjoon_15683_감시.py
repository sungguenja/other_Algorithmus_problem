N,M=map(int,input().split())

room=[0]*N
brand = [1,2,3,4,5]
direction = {1:[[0],[1],[2],[3]],2:[[0,2],[1,3]],3:[[0,1],[1,2],[2,3],[3,0]],4:[[2,3,0],[3,0,1],[0,1,2],[1,2,3]],5:[[0,1,2,3]]}
see = [[0,1],[1,0],[0,-1],[-1,0]]
last_cnt = N*M

def case(n,k,N,M):
    global last_cnt
    if n==k:        # cctv감시구역 다 체크함
        cnt = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    cnt+=1
        if cnt<last_cnt:
            last_cnt = cnt
    else:
        i,j,cam = now_cc[n]
        for direct in direction[cam]:
            watch = []
            for x in direct:
                ni=i
                nj=j
                while 0<=ni<N and 0<=nj<M and room[ni][nj] != 6:
                    if room[ni][nj] == 0:
                        room[ni][nj] = '#'
                        watch.append([ni,nj])
                    ni += see[x][0]
                    nj += see[x][1]
            case(n+1,k,N,M)
            for t in watch:
                room[t[0]][t[1]] = 0

now_cc = []
for i in range(N):
    cctv=[]
    cctv=list(map(int,input().split()))
    for j in range(M):
        if cctv[j] in brand:
            now_cc.append([i,j,cctv[j]])
    room[i] = cctv[:]
case(0,len(now_cc),N,M)
print(last_cnt)