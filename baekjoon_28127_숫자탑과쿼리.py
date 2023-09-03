from collections import deque
from sys import stdin
input = stdin.readline
N = int(input())

for _ in range(N):
    a,d,index = map(int,input().split())
    cnt = 1
    floorStart = 1
    while True:
        floorCnt = a + (cnt - 1) * d
        if floorStart + floorCnt > index:
            break
        floorStart += floorCnt
        cnt += 1
    print(cnt, index - floorStart + 1)