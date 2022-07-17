import sys
input = sys.stdin.readline

def binarySearch(score,point_status,left,right):
    mid = (left+right)//2
    if mid == left or mid == right or right - left <= 1:
        if score <= point_status[mid][1]:
            return point_status[mid][0]
        else:
            return point_status[mid+1][0]
    
    if score <= point_status[mid][1]:
        return binarySearch(score,point_status,left,mid)
    else:
        return binarySearch(score,point_status,mid+1,right)

N,M = map(int,input().split())
naming = []

for _ in range(N):
    a,b = input().split()
    b = int(b)
    naming.append([a,b])

for _ in range(M):
    score = int(input())
    print(binarySearch(score,naming,0,N))