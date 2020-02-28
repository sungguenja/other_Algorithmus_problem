while True:
    histogram = list(map(int,input().split()))
    area=[0]*len(histogram)
    if histogram == [0]:
        break
    for i in range(1,len(histogram)):
        z=1
        if histogram[i] != 1:
            for j in range(i+1,len(histogram)):
                if histogram[i]>histogram[j]:
                    break
                z+=1
            for j in range(i-1,0,-1):
                if histogram[i]>histogram[j]:
                    break
                z+=1
        else:
            z=len(histogram)-1
        area[i] = histogram[i]*z
    print(max(area))