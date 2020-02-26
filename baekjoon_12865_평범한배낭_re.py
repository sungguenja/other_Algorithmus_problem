N,K=map(int,input().split())

gram_value = [0]*N
for i in range(N):
    G,V = map(int,input().split())
    gram_value[i] = [G,V]

max_value = 0
for i in range(1<<N):
    gram=0
    value=0
    for j in range(N):
        if i&(1<<j):
            gram+=gram_value[j][0]
            value+=gram_value[j][1]
            if gram>K:
                break
    else:
        if gram<=K and max_value<value:
            max_value = value

print(max_value)