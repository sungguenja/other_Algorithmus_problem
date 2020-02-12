N=int(input())
i=0
while True:
    if 1+3*i*(i+1) >= N:
        break
    i+=1
print(i+1)