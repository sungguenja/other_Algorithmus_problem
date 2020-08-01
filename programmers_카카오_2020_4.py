answer = 99999999
direction = [[0,1],[1,0],[0,-1],[-1,0]]
def backtrack(vis,road,N,i=0,j=0,cost=0,direct=5):
    global answer
    if answer<=cost:
        return
    
    if i==N-1 and j==N-1:
        if answer>cost:
            answer = cost
        return
    
    for k in direction:
        ni = i+k[0]
        nj = j+k[1]
        if 0<=ni<N and 0<=nj<N:
            if road[ni][nj] == 0 and vis[ni][nj] == 0:
                vis[ni][nj] = 1
                if direct == 5:
                    backtrack(vis,road,N,ni,nj,cost+100,direction.index([ni-i,nj-j]))
                else:
                    if direction.index([ni-i,nj-j]) == direct or (direction.index([ni-i,nj-j])+2)%4 == direct:
                        backtrack(vis,road,N,ni,nj,cost+100,direction.index([ni-i,nj-j]))
                    else:
                        backtrack(vis,road,N,ni,nj,cost+600,direction.index([ni-i,nj-j]))
                vis[ni][nj] = 0

def solution(board):
    global answer
    N=len(board)
    visit = [[0]*N for _ in range(N)]
    backtrack(visit,board,N)
    return answer