N=int(input())
i=0
while True:
    if (3**(i+2)-1)//2 > N >= (3**(i+1)-1)//2:
        break
    i+=1

X=[]
for z in range(i,-1,-1):
    for k in range(3):
        N=N-3**z
        if N<(3**(z+1)-1)//2:
            break
    if k==2:
        X.append('4')
    elif k==1:
        X.append('2')
    elif k==0:
        X.append('1')
print(X)