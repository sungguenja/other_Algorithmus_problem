import sys
input = sys.stdin.readline
answer = {}
def solution(start,end):
    global answer
    answer_list = []
    while start < end:
        if arr[start] != arr[end]:
            return 0
        if answer.get((start,end)) != None:
            break
        answer_list.append((start,end))
        start += 1
        end -= 1
    for key in answer_list:
        answer[key] = 1
    return 1

N = int(input())
arr = list(map(int,input().split()))
for t in range(int(input())):
    start,end = map(int,input().split())
    print(solution(start-1,end-1))