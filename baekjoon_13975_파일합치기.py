from sys import stdin
import heapq
input = stdin.readline

N = int(input())

for _ in range(N):
    K = int(input())
    fileArray = list(map(int, input().split()))
    answer = 0
    que = []
    for i in fileArray:
        heapq.heappush(que,i)
    
    while len(que) > 1:
        leftFile = heapq.heappop(que)
        rightFile = heapq.heappop(que)
        answer += leftFile + rightFile
        heapq.heappush(que,leftFile+rightFile)
    print(answer)