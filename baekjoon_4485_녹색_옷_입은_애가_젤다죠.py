from collections import deque
from sys import stdin

input = stdin.readline

def findMinimumRuppy(size,cave):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [[-1]*size for _ in range(size)]
    Queue = deque()
    Queue.append([0,0,cave[0][0]])
    while Queue:
        i,j,ruppy = Queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<size and 0<=nj<size:
                if visit[ni][nj] == -1 or visit[ni][nj] > ruppy + cave[ni][nj]:
                    visit[ni][nj] = ruppy + cave[ni][nj]
                    Queue.append([ni,nj,ruppy + cave[ni][nj]])
    return visit[-1][-1]

answer = []
while True:
    size = int(input())
    if size == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(size)]
    answer.append(findMinimumRuppy(size,cave))

for ans in range(len(answer)):
    print('Problem ' + str(ans + 1) + ': ' + str(answer[ans]))