N,M=map(int,input().split())
horizontal =[0]
vertical =[0]
for _ in range(int(input())):
    way,numb=map(int, input().split())
    if way == 0:
        horizontal.append(numb)
    if way == 1:
        vertical.append(numb)

horizontal.append(M)
vertical.append(N)
horizontal.sort()
vertical.sort()
max_area = 0
for i in range(1,len(horizontal)):
    for j in range(1,len(vertical)):
        if max_area<(horizontal[i]-horizontal[i-1])*(vertical[j]-vertical[j-1]):
            max_area = (horizontal[i]-horizontal[i-1])*(vertical[j]-vertical[j-1])
print(max_area)