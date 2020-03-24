direction = [[0,1],[1,0],[0,-1],[-1,0]]

Game = [0]*12
for i in range(12):
    horizon = []
    horizon = list(input())
    Game[i] = horizon[:]

trigger=True
game_count=0
while trigger:
    visit = [[0]*6 for _ in range(12)]
    num = 0
    stack = []
    for i in range(12):
        for j in range(6):
            if Game[i][j] != '.':
                que = [[i,j,Game[i][j]]]
                cnt = 1
                visit[i][j] = 1
                stack.append([[i,j]])
                while que!=[]:
                    y,x,color=que.pop(0)

                    for k in direction:
                        ni=y+k[0]
                        nj=x+k[1]
                        if 0<=ni<12 and 0<=nj<6:
                            if Game[ni][nj] == color and visit[ni][nj]==0:
                                que.append([ni,nj,Game[ni][nj]])
                                stack[num].append([ni,nj])
                                visit[ni][nj] = 1
                                cnt+=1
                if cnt<4:
                    stack.pop(num)
                else:
                    num+=1
    if len(stack)>0:
        skip=[]
        for k in range(len(stack)):
            while stack[k] != []:
                i,j=stack[k].pop(0)
                Game[i][j] = '.'
        else:
            game_count += 1
        for i in range(11,-1,-1):
            for j in range(6):
                if j in skip:
                    continue
                if Game[i][j] == '.':
                    ni=i
                    while Game[ni][j] == '.' and ni>=0:
                        ni-=1
                    if ni>=0:
                        Game[ni][j],Game[i][j] = Game[i][j],Game[ni][j]
                    else:
                        skip.append(j)
    else:
        trigger = False
print(game_count)