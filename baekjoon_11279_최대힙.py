N=int(input())
X=[]
maximum = 0
for i in range(N):
    z=int(input())
    if z==0:
        if len(X) == 0 or X.count(0) == len(X):
            print(0)
            maximum=0
        else:
            print(X[sav_i])
            X[sav_i] = 0
            sav_i = X.index(max(X))
    else:
        if z>maximum:
            maximum = z
            sav_i=len(X)
        X.append(z)