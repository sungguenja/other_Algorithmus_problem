def merge(A,B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0])%1000000,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%1000000],[(A[1][0]*B[0][0]+A[1][1]*B[1][0])%1000000,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%1000000]]

def makeMatrix(n):
    if n<=0:
        return [[1,0],[0,1]]
    now = [[1,1],[1,2]]
    i = 1
    while i<=n:
        i *= 2
        if i>=n:
            break
        now = [[(now[0][0]*now[0][0]+now[0][1]*now[1][0])%1000000,(now[0][0]*now[0][1]+now[0][1]*now[1][1])%1000000],[(now[1][0]*now[0][0]+now[1][1]*now[1][0])%1000000,(now[1][0]*now[0][1]+now[1][1]*now[1][1])%1000000]]
    i //= 2
    return merge(now,makeMatrix(n-i))

N = int(input())
answer = makeMatrix(N//2)
start = [[0,1],[1,2]]
answer = merge(start,answer)
if N%2==0:
    print(answer[0][0]%1000000)
else:
    print(answer[0][1]%1000000)