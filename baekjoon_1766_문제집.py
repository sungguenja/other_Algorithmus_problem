from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
forked_list = [0]*(N+1)
arrow_matrix = [[] for i in range(N+1)]

for _ in range(M):
    left,right = map(int,input().split())
    for i in arrow_matrix[left]:
        if i == right:
            arrow_matrix[right].append(left)
            forked_list[right] -= 1
            forked_list[left] += 1
            break
    else:
        arrow_matrix[left].append(right)
        forked_list[right] += 1
        forked_list[left] -= 1

rank_dict = {}
for i in range(1,N+1):
    if forked_list[i] in rank_dict.keys():
        rank_dict[forked_list[i]].append(i)
    else:
        rank_dict[forked_list[i]] = [i]

rank_list = sorted(list(rank_dict.keys()))

answer = []
for i in rank_list:
    for j in rank_dict[i]:
        answer.append(str(j))

print(' '.join(answer))