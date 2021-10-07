from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

result = 0
def checkAnti(anti,now):
    left = now - 1
    while left >= 0 and anti[left] == '':
        left -= 1
    if left == -1 or len(anti[left]) == 0 or len(anti[now]) == 0:
        return False,left
    if sum(list(map(int,anti[now].split(',')))) == sum(list(map(int,anti[left].split(',')))):
        return True,left
    return False,left

def dfs(now_arr,anti,now=0):
    global result
    if now == len(now_arr):
        result += 1
        return
    
    if now != 0:
        trigger,left = checkAnti(anti,now)
        if trigger:
            dfs(now_arr,anti,now+1)
            next_arr = deepcopy(anti)
            next_arr[now] = next_arr[left]+','+next_arr[now]
            next_arr[left] = ''
            dfs(now_arr,next_arr,now)
        else:
            dfs(now_arr,anti,now+1)
    else:
        dfs(now_arr,anti,now+1)


def check(arr):
    global result
    result = 0
    str_arr = list(map(str,arr))
    dfs(arr,str_arr)

def solution(a, s):
    answer = []
    start_position = 0
    for num in s:
        check(a[start_position:start_position+num])
        start_position += num
        answer.append(result)
    return answer

print(solution([1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6],[4,3,1,5,6]))