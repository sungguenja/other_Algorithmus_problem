while True:
    arr = list(map(int,input().split()))
    if arr == [0]:
        break
    length = arr[0]
    arr = arr[1:]
    stack = [0]*len(arr)
    check = [True]*len(arr)
    maximum = -1
    r=0
    l=0
    while r < len(arr):
        X = arr[r]
        if l == 0:
            stack[l] = X
            l+=1
        else:
            save_l=l
            while stack[l-1] != 0 and stack[l-1]>X:
                if maximum<stack[l-1]*(save_l-l+1):
                    maximum = stack[l-1]*(save_l-l+1)
                stack[l-1] = 0
                l -= 1
            stack[l] = X
            l+=1
        r+=1
    if stack != [0]*len(arr):
        i=0
        while i<len(stack) and stack[i] != 0:
            if maximum<stack[i][1]-stack[i][0]:
                maximum = stack[i][1]-stack[i][0]
            i+=1
    print(maximum)