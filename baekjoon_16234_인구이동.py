from copy import deepcopy
direction = [[0,1],[1,0],[0,-1],[-1,0]]
N,L,R = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(N)]
c_world = []
day = 0
while c_world == [] or c_world != world:
    c_world = deepcopy(world)
    r_1,l_1,r_2,l_2=-1,-1,-1,-1
    que_1 = [0]*N**2
    que_2 = [0]*N**2
    visit = [[None]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == None:
                for k in direction:
                    ni = i+k[0]
                    nj = j+k[1]
                    if 0<=ni<N and 0<=nj<N:
                        if L<=abs(world[i][j]-world[ni][nj])<=R and visit[ni][nj] == None:
                            l_1+=1
                            l_2+=1
                            que_1[l_1] = [i,j,world[i][j]]
                            que_2[l_2] = [i,j]
                            visit[i][j] = 1
                            human = 0
                            country = 0
                            break
                while r_1 != l_1:
                    r_1+=1
                    X = que_1[r_1]
                    y,x,people = X[0],X[1],X[2]
                    human += people
                    country += 1
                    for k in direction:
                        ni = y+k[0]
                        nj = x+k[1]
                        if 0<=ni<N and 0<=nj<N:
                            if L<=abs(world[y][x]-world[ni][nj])<=R and visit[ni][nj] == None:
                                l_1+=1
                                l_2+=1
                                que_1[l_1] = [ni,nj,world[ni][nj]]
                                que_2[l_2] = [ni,nj]
                                visit[ni][nj] = 1
                while r_2 != l_2:
                    r_2 += 1
                    k = que_2[r_2]
                    world[k[0]][k[1]] = human//country
                que_2 = [0]*N**2
                r_2 = -1
                l_2 = -1
    if world != c_world:
        day += 1
print(day)