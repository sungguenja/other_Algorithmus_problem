import sys

input = sys.stdin.readline

N = int(input())
honey_list = list(map(int,input().split()))
all_honey = sum(honey_list)
answer = -1
tmp = honey_list[0]

for i in range(1,N):
    tmp += honey_list[i]
    answer = max(answer, (all_honey - honey_list[0]) + (all_honey - tmp - honey_list[i]))

honey_list.reverse()
tmp = honey_list[0]

for i in range(1,N):
    tmp += honey_list[i]
    answer = max(answer, (all_honey - honey_list[0]) + (all_honey - tmp - honey_list[i]))

for i in range(1,N):
    answer = max(answer, all_honey - honey_list[0] - honey_list[-1] + honey_list[i])

print(answer)