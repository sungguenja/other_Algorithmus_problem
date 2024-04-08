N = int(input())
arr = list(map(int,input().split()))
S = int(input())

for i in range(len(arr)):
    j = len(arr)
    while True:
        if i == arr.index(max(arr[i:j])):
            break
        if arr.index(max(arr[i:j]))-i <= S:
            maxIndex = arr.index(max(arr[i:j]))
            S -= maxIndex - i
            for k in range(maxIndex - 1, i - 1, -1):
                arr[k], arr[k+1] = arr[k+1], arr[k]
        else:
            j -= 1

print(' '.join(map(str, arr)))