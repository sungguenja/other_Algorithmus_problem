from copy import deepcopy
import sys
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
weight = [[INF]*N for i in range(N)]
for i in range(N):
    weight[i][i] = 0

for t in range(int(input())):
    start,end,w = map(int,input().split())
    weight[start-1][end-1] = min(weight[start-1][end-1],w)

def floyd():
    global weight
    inner_weight = deepcopy(weight)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i!=j:
                    inner_weight[i][j] = min(inner_weight[i][j],inner_weight[i][k]+inner_weight[k][j])
    
    for i in range(N):
        for j in range(N):
            if inner_weight[i][j] != INF:
                weight[i][j] = str(inner_weight[i][j])
            else:
                weight[i][j] = '0'

floyd()
for k in weight:
    print(' '.join(k))