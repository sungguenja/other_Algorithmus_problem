answer = 11
N,M = map(int,input().split())

coinList = []
board = []
for i in range(N):
    horizon = list(input())
    board.append(horizon[:])
    if len(coinList) == 2:
        continue
    for j in range(M):
        if horizon[j] == 'o':
            coinList.append([i,j])

def checkIsOut(coin):
    if coin[0] < 0 or coin[0] >= N or coin[1] < 0 or coin[1] >= M:
        return True
    return False

def checkIsIn(coin1,coin2):
    if 0<=coin1[0]<N and 0<=coin1[1]<M and 0<=coin2[0]<N and 0<=coin2[1]<M:
        return True
    return False

def moveCoin(coin,cnt=0):
    global answer
    if cnt >= answer:
        return
    if checkIsIn(coin[0],coin[1]) and (board[coin[0][0]][coin[0][1]] == '#' or board[coin[1][0]][coin[1][1]] == '#'):
        return
    
    isFirstOut = checkIsOut(coin[0])
    isSecondOut = checkIsOut(coin[1])
    if isFirstOut and isSecondOut:
        return
    if (isFirstOut and not isSecondOut) or (not isFirstOut and isSecondOut):
        answer = cnt
        return
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for k in range(4):
        coin1ni = coin[0][0] + di[k]
        coin1nj = coin[0][1] + dj[k]
        coin2ni = coin[1][0] + di[k]
        coin2nj = coin[1][1] + dj[k]
        if not checkIsIn([coin1ni,coin1nj],[coin2ni,coin2nj]):
            moveCoin([[coin1ni,coin1nj],[coin2ni,coin2nj]],cnt+1)
        elif board[coin1ni][coin1nj] == '#':
            if board[coin2ni][coin2nj] == '#':
                continue
            else:
                moveCoin([[coin[0][0],coin[0][1]],[coin2ni,coin2nj]],cnt+1)
        elif board[coin2ni][coin2nj] == '#':
            moveCoin([[coin1ni,coin1nj],[coin[1][0],coin[1][1]]],cnt+1)
        else:
            moveCoin([[coin1ni,coin1nj],[coin2ni,coin2nj]],cnt+1)
        
moveCoin(coinList)
if answer == 11:
    print(-1)
else:
    print(answer)