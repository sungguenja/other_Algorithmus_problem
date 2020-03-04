N=int(input())
print(0)
X=[]
num = 0
for _ in range(N):
    z = int(input())
    if z == 0:
        num+=1
    else:
        X.append(z)
    
    if num == 2:
        if X == []:
            print(0)
        while X!=[]:
            print(X.pop(X.index(max(X))))
        num = 0