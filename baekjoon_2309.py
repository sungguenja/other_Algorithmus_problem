X=[0]*9
for i in range(9):
    X[i] = int(input())

for i in range(8):
    for j in range(i+1,9):
        if sum(X) - X[i] - X[j] == 100:
            A=X[i]
            B=X[j]
            break

X.sort()
for i in range(9):
    if X[i] == A or X[i] == B:
        continue
    else:
        print(X[i])