answer = 5

def moving():
    for i in range(N):
        num = i
        for j in range(H):
            if num == 0:
                if bridge[j][num] == 1:
                    num += 1
            elif num == N-1:
                if bridge[j][num-1] == 1:
                    num -= 1
            else:
                if bridge[j][num] == 1:
                    num += 1
                elif bridge[j][num-1] == 1:
                    num -= 1
        if num != i:
            return False
    return True

def solution(amount,idx=-1,cnt=0):
    global answer
    if amount == cnt:
        if moving():
            if answer > amount:
                answer = amount
        return
    
    for i in range(idx+1,len(can)):
        y,x = can[i]
        if x == 0:
            if bridge[y][x+1] == 0:
                bridge[y][x] = 1
                solution(amount,i,cnt+1)
                bridge[y][x] = 0
        elif x == N-1:
            if bridge[y][x-1] == 0:
                bridge[y][x] = 1
                solution(amount,i,cnt+1)
                bridge[y][x] = 0
        else:
            if bridge[y][x] == 0 and bridge[y][x-1] == 0 and bridge[y][x+1] == 0:
                bridge[y][x] = 1
                solution(amount,i,cnt+1)
                bridge[y][x] = 0
    
N,M,H=map(int,input().split())
bridge = [[0]*N for i in range(H)]

can = [[i,j] for i in range(H) for j in range(N)]

for i in range(M):
    y,x = map(int,input().split())
    bridge[y-1][x-1] = 1
    can.remove([y-1,x-1])

for i in range(4):
    solution(i)
    if answer != 5:
        print(answer)
        break

if answer == 5:
    print(-1)