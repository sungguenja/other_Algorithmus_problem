import sys
def findTree(weight,N):
    g_cnt = 0
    d_cnt = 0
    for now in range(N):
        cnt = len(weight[now])
        if cnt >= 3:
            g_cnt += ((cnt)*(cnt-1)*(cnt-2))//6
        if cnt >= 2:
            loop_cnt = 0
            for goal in range(cnt):
                loop_cnt += 1
                goal = weight[now][goal]
                d_cnt += (len(weight[goal])-1)*(cnt-1)
    return g_cnt,d_cnt//2


N = int(sys.stdin.readline())
weight = [[] for i in range(N)]
for i in range(N-1):
    start,end = map(int,sys.stdin.readline().split())
    weight[start-1].append(end-1)
    weight[end-1].append(start-1)

g_tree,d_tree = findTree(weight,N)
if g_tree*3 < d_tree:
    print('D')
elif g_tree*3 == d_tree:
    print('DUDUDUNGA')
else:
    print('G')