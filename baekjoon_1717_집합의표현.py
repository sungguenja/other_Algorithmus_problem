from sys import stdin
input = stdin.readline

def findWhereAmI(array,start):
    before_start = start
    while array[start] != -1:
        start = array[start]
        if before_start == start:
            break
        before_start = start
    
    return start

def sumSet(array,left,right):
    if left == right:
        return array

    left = findWhereAmI(array,left)
    right = findWhereAmI(array,right)

    if left == right:
        return array

    array[left] = left
    array[right] = left

    return array

def isSameSet(array,left,right):
    if left == right:
        return "YES"
    left = findWhereAmI(array,left)
    right = findWhereAmI(array,right)

    if left == right:
        return "YES"
    else:
        return "NO"

N,M = map(int,input().split())
arr = [-1]*(N+1)

for _ in range(M):
    calculation, first_target, second_target = map(int,input().split())
    if calculation == 0:
        arr = sumSet(arr,first_target,second_target)
    else:
        print(isSameSet(arr,first_target,second_target))