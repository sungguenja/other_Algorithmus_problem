from copy import deepcopy
import sys
input = sys.stdin.readline

N,B = map(int,input().split())
A = [0]*N

for i in range(N):
    A[i] = list(map(int,input().split()))

def merge_sort(left,right):
    now = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                now[i][j] += left[i][k]*right[k][j]
            now[i][j] %= 1000
            
    return now

def solution(A,B):
    if B == 1:
        return A
    left = deepcopy(A)
    left_N = 1
    while B//left_N > 1:            # 왼쪽에 곱해지는 것을 먼저 2배씩 증가
        left = merge_sort(left,left)
        left_N *= 2
    if B%left_N == 0:               # 왼쪽이 최대한 하고 남은 나머지 처리
        right = [[0]*N for i in range(N)]
        for i in range(N):
            right[i][i] = 1
    else:
        right = solution(A,B%left_N)
    print("=====",left_N,B%left_N)
    for i in range(N):
        print(left[i],right[i])
    return merge_sort(left,right)

answer = solution(A,B)

for i in range(N):
    for j in range(N):
        answer[i][j] = str(answer[i][j]%1000)

for k in answer:
    print(" ".join(k))