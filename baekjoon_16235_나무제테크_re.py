di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
food = [list(map(int,input().split())) for _ in range(N)]
tree = [list(map(int,input().split())) for _ in range(M)]
c_food = [[5]*N for _ in range(N)]
for _ in range(K):
    tree = sorted(tree, key=lambda x: x[2])
    live_tree = [0]*len(tree)
    j = 0
    # 봄 여름
    print(c_food)
    for i in range(len(tree)):
        x,y,z = tree[i]
        if c_food[x-1][y-1] - z < 0:
            c_food[x-1][y-1] += z//2
        else:
            c_food[x-1][y-1] -= z
            live_tree[j] = [x,y,z+1]
            j+=1
    print(c_food)
    # 가을
    live_tree = live_tree[:j]
    new_tree = [0]*(len(live_tree)*8)
    m=0
    for i in range(j):
        x,y,z = live_tree[i]
        if z%5==0:
            for k in range(8):
                ni = x+di[k]
                nj = y+dj[k]
                if 0<ni<=N and 0<nj<=N:
                    new_tree[m] = [ni,nj,1]
                    m+=1
    new_tree = new_tree[:m]
    # 겨울
    for i in range(N):
        for j in range(N):
            c_food[i][j] += food[i][j]
    tree = live_tree + new_tree
print(len(tree))