answer = 99999999
direction = [[0,1],[1,0],[0,-1],[-1,0]]
def backtrack(vis,road,N,i=0,j=0,cnt=0):
    global answer
    if answer<=cnt:
        return
    
    if i==N-1 and j==N-1:
        if answer>cnt:
            answer = cnt
        return
    
    for k in direction:
        ni = i+k[0]
        nj = j+k[1]
        if 0<=ni<N and 0<=nj<N:
            if road[ni][nj] == 0 and vis[ni][nj] == 0:
                vis[ni][nj] = 1
                backtrack(vis,road,N,ni,nj,cnt+1)
                vis[ni][nj] = 0

def solution(board):
    global answer
    N=len(board)
    visit = [[0]*N for _ in range(N)]
    backtrack(visit,board,N)
    return answer

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))