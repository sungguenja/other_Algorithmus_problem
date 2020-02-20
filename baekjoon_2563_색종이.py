paper = [[None]*100 for _ in range(100)]

size = 0

for t in range(int(input())):
    X,Y=map(int,input().split())
    for i in range(Y,Y+10):
        for j in range(X,X+10):
            if paper[i][j] == None:
                size += 1
                paper[i][j] = 0
            else:
                continue
print(size)