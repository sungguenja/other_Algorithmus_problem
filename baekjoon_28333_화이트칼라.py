from collections import deque
from sys import stdin
input = stdin.readline
T = int(input())

def bfs(N,road):
    answer = set()
    answerCnt = N**2
    visit = [[-1] * N for i in range(N)]
    Que = deque()
    Que.append([0,0,[1]])
    while Que:
        start,cnt,visited = Que.popleft()
        if cnt > answerCnt:
            continue
        if start == N - 1:
            if cnt < answerCnt:
                answerCnt = cnt
                answer = set(visited)
            if cnt == answerCnt:
                answer.update(visited)
            continue
        for end in road[start]:
            if visit[start][end] == -1 or visit[start][end] >= cnt + 1:
                visit[start][end] = cnt + 1
                Que.append([end,cnt+1,visited + [end + 1]])
    return answer

for _ in range(T):
    N,M = map(int,input().split())
    road = [[] for i in range(N)]
    for c in range(M):
        i,j = map(int,input().split())
        road[i-1].append(j-1)
    print(' '.join(map(str,bfs(N,road))))