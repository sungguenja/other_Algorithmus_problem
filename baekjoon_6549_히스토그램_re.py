def solution(arr,start,end):
    if start == end:
        return arr[start]
    mid = (start+end)//2
    height = min(arr[mid],arr[mid+1])
    squre = height*2
    cnt = 2
    left = mid
    right = mid+1
    while True:
        if (arr[left] == 0 or left == start) and (arr[right] == 0 or right == end):
            break
        if arr[left] == 0 or left == start:
            height = min(height,arr[right+1])
            right += 1
        elif arr[right] == 0 or right == end:
            height = min(height,arr[left-1])
            left -= 1
        else:
            if arr[left - 1] > arr[right + 1]:
                height = min(height,arr[left-1])
                left -= 1
            else:
                height = min(height,arr[right+1])
                right += 1
        cnt += 1
        squre = max(squre,height*cnt)
    return max(squre,solution(arr,start,mid),solution(arr,mid+1,end))


while True:
    arr = list(map(int,input().split()))
    if arr == [0]:
        break
    print(solution(arr,1,len(arr)-1))