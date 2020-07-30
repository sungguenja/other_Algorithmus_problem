from copy import deepcopy
di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
food = [list(map(int,input().split())) for _ in range(N)]
tree = [list(map(int,input().split())) for _ in range(M)]
c_food = [[5]*N for _ in range(N)]
for _ in range(K):
    tree = sorted(tree, key=lambda x: x[2])
    live_tree = [0]*len(tree)
    dead_tree = [0]*len(tree)
    j = 0
    k = 0
    # 봄
    for i in range(len(tree)):
        x,y,z = tree[i]
        if c_food[x-1][y-1] - z < 0:
            dead_tree[j] = [x,y,z]
            j+=1
        else:
            c_food[x-1][y-1] -= z
            live_tree[k] = [x,y,z+1]
            k+=1
    # 여름
    for i in range(len(dead_tree)):
        if dead_tree[i] == 0:
            break
        x,y,z = dead_tree[i]
        c_food[x-1][y-1] += z//2
    # 가을
    for i in range(len(tree)):
        if live_tree[i]==0:
            r=i
            break
    else:
        r=len(tree)
    new_tree = [0]*len(live_tree)*8
    l = 0
    for i in range(r):
        x,y,z = live_tree[i]
        if z%5==0:
            for m in range(8):
                ni = x+di[m]
                nj = y+dj[m]
                if 0<ni<=N and 0<nj<=N:
                    new_tree[l] = [ni,nj,1]
                    l+=1
    if 0 in live_tree:
        live_tree = live_tree[:k]
    if 0 in new_tree:
        new_tree = new_tree[:l]
    # 겨울
    for i in range(N):
        for j in range(N):
            c_food[i][j] += food[i][j]
    tree = live_tree+new_tree
print(len(tree))