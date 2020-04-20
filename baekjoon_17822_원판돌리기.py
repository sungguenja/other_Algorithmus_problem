direction = [[0,1],[1,0],[0,-1],[-1,0]]
N,M,K = map(int,input().split())
circle = [0]*N
for i in range(N):
    circle[i] = list(map(int,input().split()))

command = [0]*K

for i in range(K):
    command[i] = list(map(int,input().split()))

for order in command:
    print('돌리기전',circle)
    for i in range(N):
        if (i+1)%order[0] == 0:
            if order[1] == 0:
                for _ in range(order[2]):
                    saving = circle[i][M-1]
                    for j in range(M-1,0,-1):
                        circle[i][j] = circle[i][j-1]
                    circle[i][0] = saving
            else:
                for _ in range(order[2]):
                    saving = circle[i][0]
                    for j in range(M-1):
                        circle[i][j] = circle[i][j+1]
                    circle[i][M-1] = saving
    print('돌리고',circle)
    trigger = True
    for i in range(N):
        for j in range(M):
            if circle[i][j] != 0:
                for k in direction:
                    ni = i+k[0]
                    nj = j+k[1]
                    if 0<=ni<N and -1<=nj<=M:
                        if circle[i][j] == circle[ni][nj%M]:
                            trigger = False
                            circle[i][j] = 0
                            circle[ni][nj%M] = 0
    print('바뀜',circle)
    if trigger:
        print('hi')
        score = 0
        cnt = 0
        stack = [0]*N*M
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 0:
                    stack[cnt] = [i,j]
                    cnt += 1
                    score += circle[i][j]
        for k in stack:
            if k == 0:
                break
            else:
                if circle[k[0]][k[1]] != 0:
                    if circle[k[0]][k[1]] > score/cnt:
                        circle[k[0]][k[1]]-=1
                    elif 0<circle[k[0]][k[1]] < score/cnt:
                        circle[k[0]][k[1]]+=1
    print(trigger,circle)


answer = 0
for k in circle:
    print(k)
    answer += sum(k)
print(answer)