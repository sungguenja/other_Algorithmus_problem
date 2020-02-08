N,M,L=map(int, input().split())
youngsik = [0]*N
i=0
count = -1
while M not in youngsik:
    if youngsik[i]%2 == 0:
        youngsik[i] += 1
        i += L
        print(youngsik)
    else:
        youngsik[i] += 1
        i -= L
        print(youngsik)
    if i >= N:
        i = i%N
    elif i < 0:
        i += N
    count += 1
print(count)