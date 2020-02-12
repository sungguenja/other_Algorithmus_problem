N=int(input())

i=0
while True:
    if N < 1 + i*(i+1)//2:
        X=1+(i-1)*i//2
        z= i-1
        break
    i+=1

Z=1
while X!=N:
    Z+=1
    i-=1
    X+=1
if z%2==1:
    print('{0}/{1}'.format(Z,i))
else:
    print('{0}/{1}'.format(i,Z))