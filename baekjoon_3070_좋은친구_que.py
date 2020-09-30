import sys
from collections import deque
N,K = map(int,sys.stdin.readline()[:-1].split())
student = [0]*N
word_que = [deque() for i in range(21)]
answer = 0
for rank in range(N):
    now = len(sys.stdin.readline()[:-1])
    student[rank] = now
    if rank>K:
        word_que[student[rank-K-1]].popleft()
    answer += len(word_que[now])
    word_que[now].append(rank)
print(answer)