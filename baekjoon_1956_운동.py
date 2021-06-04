import copy
import sys
from copy import deepcopy
input = sys.stdin.readline
INF = sys.maxsize
V,E = map(int,input().split())
route = [[INF]*(V+1) for i in range(V+1)]
for e in range(E):
    start,goal,cost = map(int,input().split())
    route[start][goal] = min(route[start][goal],cost)

def floyd():
    result = INF
    copy_route = deepcopy(route)
    for k in range(1,V+1):
        for i in range(1,V+1):
            for j in range(1,V+1):
                copy_route[i][j] = min(copy_route[i][j],copy_route[i][k]+copy_route[k][j])
    
    for i in range(1,V+1):
        for j in range(1,V+1):
            result = min(result,copy_route[i][j]+copy_route[j][i])
    if result == INF:
        result = -1
    return result

print(floyd())