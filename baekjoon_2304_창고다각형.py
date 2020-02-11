true_warehoust = [0]*1001

largest = -1
shortest = 1002

for _ in range(int(input())):
    N,M = map(int,input().split())
    true_warehoust[N] = M
    if N>largest:
        largest = N
    if N<shortest:
        shortest = N

fake_warehouse = true_warehoust[shortest:largest+1] # 필요한 부분만 자르기
z=fake_warehouse[0]
x=fake_warehouse.index(max(fake_warehouse))
for i in range(1,x):                                # 최대값의 왼쪽부터
    if z<fake_warehouse[i]:
        z=fake_warehouse[i]
    else:
        fake_warehouse[i]=z

z=fake_warehouse[-1]
for i in range(len(fake_warehouse)-1,x,-1):         # 최대값의 오른쪽부터
    if z<fake_warehouse[i]:
        z=fake_warehouse[i]
    else:
        fake_warehouse[i]=z

print(sum(fake_warehouse))