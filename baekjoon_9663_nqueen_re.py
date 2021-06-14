def checkQueen(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x - i:
            return False
    return True

def putQueen(x):
    global answer

    if x == N:
        answer += 1
        return
    
    for i in range(N):
        row[x] = i
        if checkQueen(x):
            putQueen(x+1)
answer = 0
N = int(input())
row = [-1]*N
putQueen(0)
print(answer)