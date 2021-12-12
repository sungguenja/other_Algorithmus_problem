from collections import deque
for _ in range(int(input())):
    N = int(input())
    last_year_rank = list(map(int,input().split()))
    this_year_rank = []
    forked_list = [0]*(N+1)
    arrow_matrix = [[] for _ in range(N+1)]
    for i in range(N-1):
        for j in range(i+1,N):
            arrow_matrix[last_year_rank[i]].append(last_year_rank[j])
            forked_list[last_year_rank[j]] += 1
    for state in range(int(input())):
        left,right = map(int,input().split())
        for i in arrow_matrix[left]:
            if i == right:
                arrow_matrix[left].remove(right)
                arrow_matrix[right].append(left)
                forked_list[right] -= 1
                forked_list[left] += 1
                break
        else:
            arrow_matrix[right].remove(left)
            arrow_matrix[left].append(right)
            forked_list[left] -= 1
            forked_list[right] += 1
    Que = deque()
    for i in range(1,N+1):
        if forked_list[i] == 0:
            Que.append(i)

    result = True
    if not Que:
        result = False
    while Que:
        if len(Que) > 1:
            result = False
            break
        start = Que.popleft()
        this_year_rank.append(str(start))
        for i in arrow_matrix[start]:
            forked_list[i] -= 1
            if forked_list[i] == 0:
                Que.append(i)
            elif forked_list[i] < 0:
                result = False
                break
    
    if not result or len(this_year_rank) < N:
        print('IMPOSSIBLE')
    else:
        print(' '.join(this_year_rank))