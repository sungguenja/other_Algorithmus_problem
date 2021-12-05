from collections import deque
N,M=map(int,input().split())

arrow_matrix = [[] for i in range(N+1)]
forked_list = [0]*(N+1)
line_list = []

for i in range(M):
    left,right = map(int,input().split())
    forked_list[right] += 1
    arrow_matrix[left].append(right)

Que = deque()
for start in range(1,N+1):
    if forked_list[start] == 0:
        Que.append(start)

while Que:
    start = Que.popleft()
    line_list.append(str(start))
    for end in arrow_matrix[start]:
        forked_list[end] -= 1
        if forked_list[end] == 0:
            Que.append(end)
            
print(' '.join(line_list))