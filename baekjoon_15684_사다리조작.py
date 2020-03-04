import copy

def game(N,M):
    global c_bridge

    for j in range(N):
        ni=0
        nj=j
        goal = 5
        while ni != M:
            if c_bridge[ni][nj] == 1 and goal != 0:
                while c_bridge[ni][nj] == 1:
                    nj+=1
                goal=1
            if nj-1>=0 and c_bridge[ni][nj-1] == 1 and goal != 1:
                while nj-1>=0 and c_bridge[ni][nj-1]==1:
                    nj-=1
                goal=0
            if c_bridge[ni][nj]==0 or goal!=2:
                ni+=1
                goal=2
        if nj!=j:
            break
    else:
        return True
    return False 


N,B,M=map(int,input().split())
bridge = [[0]*N for _ in range(M)]
for _ in range(B):
    y,x=map(int,input().split())
    bridge[y-1][x-1] = 1
can=[]
for i in range(M):
    for j in range(N-1):
        if bridge[i][j] == 0:
            can.append([i,j])

result = False
p_res = -1
for j in range(N-1):
    ni=0
    nj=j
    while ni!=M:
        if bridge[ni][nj] == 0:
            ni+=1
        else:
            if nj-1>=0 and bridge[ni][nj-1]==1:
                nj-=1
            else:
                nj+=1
                if nj==N:
                    nj-=1
    if nj!=j:
        break
else:
    result = True
    p_res = 0     

for i in range(len(can)):
    if result:
        break
    c_bridge=copy.deepcopy(bridge)
    now=can[i]
    c_bridge[now[0]][now[1]] = 1
    if game(N,M):
        result = True
        p_res = 1

for i in range(len(can)-1):
    if result:
        break
    for j in range(i+1,len(can)):
        if j == i+1:
            continue
        if result:
            break
        c_bridge=copy.deepcopy(bridge)
        now=can[i]
        c_bridge[now[0]][now[1]] = 1
        now=can[j]
        c_bridge[now[0]][now[1]] = 1
        if game(N,M):
            result = True
            p_res = 2

for i in range(len(can)-2):
    if result:
        break
    for j in range(i+1,len(can)-1):
        if result:
            break
        if j==i+1:
            continue
        for k in range(j+1,len(can)):
            if result:
                break
            if k == j+1:
                continue
            c_bridge=copy.deepcopy(bridge)
            now=can[i]
            c_bridge[now[0]][now[1]] = 1
            now=can[j]
            c_bridge[now[0]][now[1]] = 1
            now=can[k]
            c_bridge[now[0]][now[1]] = 1
            if game(N,M):
                result = True
                p_res = 3
print(p_res)