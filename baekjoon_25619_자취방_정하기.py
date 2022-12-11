from collections import deque
from sys import stdin

input = stdin.readline

N,M = map(int,input().split())
room_list = [[float('inf')]*N for _ in range(N)]
trigger = False

for _ in range(M):
    start,end,a,b = map(int,input().split())
    room_list[start-1][end-1] = (a+b)/2
    room_list[end-1][start-1] = (a+b)/2
    if (a+b) / 2 < 0 and (start == 1 or end == 1):
        trigger = True
        print((a+b)/2)

max_length = int(input())

if (trigger):
    print(N-1)
    for i in range(2,N+1):
        print(i, end=' ')
else:
    answer = set()
    Queue = deque()
    Queue.append([0,0])
    while Queue:
        start, cost = Queue.popleft()
        for i in range(N):
            if cost + room_list[start][i] <= max_length:
                answer.add(i)
                if i >= start and cost + room_list[start][i] > 0:
                    Queue.append([i,cost+room_list[start][i]])
    print(len(answer))
    if len(answer) > 0:
        for ans in answer:
            print(ans + 1,end=' ')