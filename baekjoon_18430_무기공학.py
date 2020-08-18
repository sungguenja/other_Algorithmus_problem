# N,M = map(int,input().split())
# board = [list(map(int,input().split())) for _ in range(N)]
# answer = 0
# direction = [[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]],[[-1,0],[0,1]]]
# visit = [[0]*M for _ in range(N)]
# def solution(cost=0):
#     global answer
#     if answer<cost:
#         print(visit)
#         answer = cost
    
#     trigger = False
#     can_case = []
#     for i in range(N):
#         for j in range(M):
#             if visit[i][j] == 0:
#                 for k in range(len(direction)):
#                     ni = i + direction[k][0][0]
#                     nj = j + direction[k][0][1]
#                     nni = i + direction[k][1][0]
#                     nnj = j + direction[k][1][1]
#                     if 0<=ni<N and 0<=nj<M and 0<=nni<N and 0<=nnj<M and visit[ni][nj]==0 and visit[nni][nnj]==0:
#                         trigger = True
#                         can_case.append(k)
#                 if trigger:
#                     break
#         if trigger:
#             break
    
#     if trigger:
#         now = board[i][j]*2
#         visit[i][j]=1
#         for k in can_case:
#             ni = i + direction[k][0][0]
#             nj = j + direction[k][0][1]
#             nni = i + direction[k][1][0]
#             nnj = j + direction[k][1][1]
#             visit[ni][nj]=1
#             visit[nni][nnj]=1
#             solution(cost+now+board[ni][nj]+board[nni][nnj])
#             visit[ni][nj]=0
#             visit[nni][nnj]=0
#         visit[i][j]=0
# solution()
# print(answer)
# 위는 전에 체크한 부분을 계속 검사해서 시간초과
# 아래는 pypy에서 통과함 python은 안됨
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
direction = [[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]],[[-1,0],[0,1]]]
visit = [[0]*M for _ in range(N)]
def solution(y=-1,x=-1,cost=0):
    global answer
    if answer<cost:
        answer = cost
    
    for i in range(N):
        for j in range(M):
            if i<=y and j<=x:
                continue
            if visit[i][j] == 0:
                visit[i][j]=1
                now = board[i][j]*2
                for k in range(len(direction)):
                    ni = i + direction[k][0][0]
                    nj = j + direction[k][0][1]
                    nni = i + direction[k][1][0]
                    nnj = j + direction[k][1][1]
                    if 0<=ni<N and 0<=nj<M and 0<=nni<N and 0<=nnj<M and visit[ni][nj]==0 and visit[nni][nnj]==0:
                        visit[ni][nj]=1
                        visit[nni][nnj]=1
                        solution(i,j,cost+now+board[ni][nj]+board[nni][nnj])
                        visit[ni][nj]=0
                        visit[nni][nnj]=0
                visit[i][j]=0
solution()
print(answer)