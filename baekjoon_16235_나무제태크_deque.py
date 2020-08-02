from collections import deque
di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
S2D2 = [list(map(int,input().split())) for _ in range(N)]
tree = {(i,j): deque() for i in range(N) for j in range(N)}
for _ in range(M):
    x,y,z=map(int,input().split())
    tree[(x-1,y-1)].append(z)
nutrition = [[5]*N for _ in range(N)]
for _ in range(K):
    # 봄 여름
    for (x,y),tree_age in tree.items():
        temp = deque()
        dead_tree = 0
        for age in tree_age:
            if age<=nutrition[x][y]:
                nutrition[x][y]-=age
                temp.append(age+1)
            else:
                dead_tree += age//2
        tree[(x,y)] = temp
        nutrition[x][y] += dead_tree
    # 가을
    new_tree = []
    for (x,y),tree_age in tree.items():
        for age in tree_age:
            if age%5==0:
                for k in range(8):
                    ni = x+di[k]
                    nj = y+dj[k]
                    if 0<=ni<N and 0<=nj<N:
                        new_tree.append((ni,nj))
    for (x,y) in new_tree:
        tree[(x,y)].appendleft(1)
    # 겨울
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += S2D2[i][j]

answer = 0
for tree_cnt in tree.values():
    answer += len(tree_cnt)
print(answer)