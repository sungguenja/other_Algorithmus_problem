N=int(input())
person = []
for i in range(N):
    w,h=map(int,input().split())
    person.append([w,h,i])

for i in range(N):
    num=1
    for j in range(N):
        if i==j:
            continue
        if person[i][0]<person[j][0] and person[i][1]<person[j][1]:
            num+=1
    print(num, end=' ')