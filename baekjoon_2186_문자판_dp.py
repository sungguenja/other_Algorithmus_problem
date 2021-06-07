from sys import stdin
input = stdin.readline
di = [1,0,-1,0]
dj = [0,1,0,-1]

N,M,K = map(int,input().split())
word_board = [list(input().strip()) for _ in range(N)]
find_word = input().strip()
length = len(find_word)
memoization = [[[-1]*length for _ in range(M)] for _ in range(N)]

def dfs(i,j,idx):
    if idx == length:
        return 1
        
    if memoization[i][j][idx] != -1:
        return memoization[i][j][idx]
    
    memoization[i][j][idx] = 0
    for d in range(4):
        for for_k in range(1,K+1):
            ni = i + for_k*di[d]
            nj = j + for_k*dj[d]
            if 0<=ni<N and 0<=nj<M:
                if word_board[ni][nj] == find_word[idx]:
                    memoization[i][j][idx] += dfs(ni,nj,idx+1)
            else:
                break
    
    return memoization[i][j][idx]

answer = 0
for i in range(N):
    for j in range(M):
        if word_board[i][j] == find_word[0]:
            answer += dfs(i,j,1)

print(answer)