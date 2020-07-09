camera = {1:[[0],[1],[2],[3]],2:[[0,2],[1,3]],3:[[0,1],[1,2],[2,3],[3,0]],4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],5:[[0,1,2,3]]}
di = [0,1,0,-1]
dj = [1,0,-1,0]

N,M = map(int,input().split())
guide = [0]*N
camera_case = []
for i in range(N):
    guide[i] = list(map(int,input().split()))
    for j in range(M):
        if 1<=guide[i][j]<=5:
            camera_case.append([i,j,guide[i][j]])
answer = N*M

def solution(camera_cnt,N,M,now=0):
    global answer
    if camera_cnt == now:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if guide[i][j] == 0:
                    cnt += 1
        if answer>cnt:
            answer = cnt
        return

    y = camera_case[now][0]
    x = camera_case[now][1]
    for case in camera[camera_case[now][2]]:
        watch = []
        for k in case:
            ni = y
            nj = x
            while 0<=ni<N and 0<=nj<M and guide[ni][nj] != 6:
                if guide[ni][nj] == 0:
                    guide[ni][nj] = '#'
                    watch.append([ni,nj])
                ni += di[k]
                nj += dj[k]
        solution(camera_cnt,N,M,now+1)
        for k in watch:
            guide[k[0]][k[1]] = 0

solution(len(camera_case),N,M)
print(answer)