n,k=map(int,input().split())

backpack = [[0]*(k+1) for _ in range(n+1)]

weight = [0]
value = [0]
for _ in range(n):
    G,V=map(int,input().split())
    weight.append(G)
    value.append(V)

for i in range(1,n+1):
    for j in range(k,-1,-1):
        if j-weight[i]>=0:
            backpack[i][j] = max(backpack[i-1][j], value[i]+backpack[i-1][j-weight[i]])
        else:
            backpack[i][j] = backpack[i-1][j]

print(max(backpack[n]))