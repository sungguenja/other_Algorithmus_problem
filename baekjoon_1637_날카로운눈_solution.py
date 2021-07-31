from sys import stdin,maxsize
input = stdin.readline
minimum = maxsize
maximum = -1

def binarySearch(minimum,maximum,N):
    left = minimum
    right = maximum

    while left < right:
        mid = (left + right) // 2

        accumulated_sum = getAccumulatedSum(mid,N)

        if accumulated_sum & 1:
            right = mid
        else:
            left = mid + 1
            
    if left >= maximum:
        print('NOTHING')
    else:
        print("{0} {1}".format(left,getAccumulatedSum(left,N) - getAccumulatedSum(left-1,N)))

def getAccumulatedSum(mid,N):
    total_sum = 0
    for i in range(N):
        if (mid >= A_list[i]):
            total_sum += (min(mid,C_list[i]) - A_list[i]) // B_list[i] + 1
    return total_sum

N = int(input())
A_list = [0]*N
B_list = [0]*N
C_list = [0]*N
for i in range(N):
    A,C,B = map(int,input().split())
    A_list[i] = A
    B_list[i] = B
    C_list[i] = C
    if A < minimum:
        minimum = A
    if C > maximum:
        maximum = C
maximum += 1
binarySearch(minimum,maximum,N)