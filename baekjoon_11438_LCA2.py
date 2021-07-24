from sys import stdin
input = stdin.readline

N = int(input())
node_list = [-1]*(N+1)
rank_list = [-1]*(N+1)
parent_list = [[] for i in range(N+1)]
node_list[1] = 0
rank_list[1] = 0
for i in range(N-1):
    a,b = map(int,input().split())
    if node_list[a] != -1:
        node_list[b] = a
        rank_list[b] = rank_list[a] + 1
        check = a
        while check != 0:
            parent_list[b].append(check)
            check = node_list[check]
    else:
        node_list[a] = b
        rank_list[a] = rank_list[b] + 1
        check = b
        while check != 0:
            parent_list[a].append(check)
            check = node_list[check]
M = int(input())
for k in range(M):
    start_1,start_2 = map(int,input().split())
    if rank_list[start_1] > rank_list[start_2]:
        for k in parent_list[start_1]:
            if k in parent_list[start_2] or start_2 == k or start_1 == k:
                print(k)
                break
    else:
        for k in parent_list[start_2]:
            if k in parent_list[start_1] or start_2 == k or start_1 == k:
                print(k)
                break