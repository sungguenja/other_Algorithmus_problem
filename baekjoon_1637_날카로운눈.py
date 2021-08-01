from sys import stdin
input = stdin.readline

N = int(input())
answer = -1
cnt = 0
arr = [False]
def inputArr(start,difference,maximum_limit):
    global answer,cnt
    while start <= maximum_limit:
        arr[start] = not arr[start]
        if arr[start]:
            answer = start
            cnt = arr[start]
        elif start == answer:
            answer = -1
            cnt = 0
        start += difference

for _ in range(N):
    A,C,B = map(int,input().split())
    if len(arr) <= C:
        arr += [False]*(C-len(arr)+1)
    inputArr(A,B,C)

if answer != -1:
    print('{0} {1}'.format(answer,cnt))
else:
    print('NOTHING')