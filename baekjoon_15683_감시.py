N,M=map(int,input().split())

room=[0]*N
brand = [1,2,3,4,5]
now_cc = []
for i in range(N):
    cctv=[]
    cctv=list(map(int,input().split()))
    for j in range(M):
        if cctv[j] in brand:
            now_cc.append([i,j,cctv[j]])
    room[i] = cctv

visit_room = [[0]*M for _ in range(N)]
for cc in range(len(now_cc)):
    