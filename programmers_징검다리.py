import sys
def binaryStone(mid,rocks,n):
    cnt = 0
    start = 0
    min_distance = sys.maxsize
    for i in range(1,len(rocks)):
        if rocks[i] - rocks[start] < mid:
            cnt += 1
        else:
            min_distance = min(min_distance,rocks[i] - rocks[start])
            start = i
    if cnt > n:
        return (False,-1)
    return (True,min_distance)

def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.append(0)
    rocks.sort()
    answer = 0
    left = 0
    right = distance
    mid = (left + right) // 2
    while left <= right:
        trigger,min_distance = binaryStone(mid,rocks,n)
        if trigger:
            answer = min_distance
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return answer