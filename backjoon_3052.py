rest =[0]*42
for _ in range(10):
    N=int(input())
    rest[N%42] += 1
counting = 0
for i in range(42):
    if rest[i] >0:
        counting += 1
print(counting)