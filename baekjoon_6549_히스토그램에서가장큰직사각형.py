import sys
def histogram(arr,start,end):
    if start == end:
        return arr[start]
    
    mid = (start + end)//2
    left = mid
    right = mid + 1
    now_hight = min(arr[left],arr[right])
    tmp = now_hight * 2
    bottom_length = 2
    while True:
        if (arr[left] == 0 or left == start) and (arr[right] == 0 or right == end):
            break
        if arr[left] == 0 or left == start:
            if arr[right + 1] < now_hight:
                now_hight = arr[right + 1]
            right += 1
        elif arr[right] == 0 or right == end:
            if arr[left - 1] < now_hight:
                now_hight = arr[left - 1]
            left -= 1
        else:
            if arr[left - 1] > arr[right + 1]:
                now_hight = min(now_hight,arr[left - 1])
                left -= 1
            else:
                now_hight = min(now_hight,arr[right + 1])
                right += 1
        bottom_length += 1
        tmp = max(tmp,now_hight*bottom_length)
    return max(histogram(arr,start,mid),histogram(arr,mid+1,end),tmp)

while True:
    now = list(map(int,sys.stdin.readline().split()))
    if now[0] == 0:
        break
    print(histogram(now,1,len(now)-1))