from sys import stdin
input = stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    tmp = (x2-x1)*(y3-y1)- (x3-x1)*(y2-y1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def isItCross(x1,y1,x2,y2,x3,y3,x4,y4):
    if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) == 0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)==0:
        if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
            return True
    elif ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)<=0:
        return True
    
    return False

def find(x):
    if parent[x]<0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

N = int(input())
point = [list(map(int,input().split())) for _ in range(N)]
answer = []
parent = [-1]*N
for i in range(N):
    for j in range(i+1,N):
        if isItCross(point[i][0],point[i][1],point[i][2],point[i][3],point[j][0],point[j][1],point[j][2],point[j][3]):
            union(i,j)

cnt = 0
answer = 0
for i in range(N):
    if parent[i]<0:
        cnt += 1
        answer = max(answer,-parent[i])

print(cnt)
print(answer)