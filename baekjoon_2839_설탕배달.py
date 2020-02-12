N=int(input())
min_plastic = N
for i in range(N//5+1):
    for j in range(N//3+1):
        if 5*i+3*j==N and i+j<min_plastic:
            min_plastic = i+j
if min_plastic==N:
    print(-1)
else:
    print(min_plastic)