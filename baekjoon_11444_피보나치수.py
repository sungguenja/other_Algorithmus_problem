def conquer(A,B):
    return [
        [(A[0][0]*B[0][0]+A[0][1]*B[1][0])%1000000007,(A[0][0]*B[0][1]+A[0][1]*B[1][1])%1000000007],
        [(A[1][0]*B[0][0]+A[1][1]*B[1][0])%1000000007,(A[1][0]*B[0][1]+A[1][1]*B[1][1])%1000000007]
    ]
def divide(N):
    if N == 0:
        return [[1,0],[0,1]]
    
    cnt = 1
    now = [[1,1],[1,2]]
    while cnt <= N:
        cnt *= 2
        if cnt >= N:
            break
        now = [
            [(now[0][0]**2 + now[0][1]*now[1][0])%1000000007,(now[0][0]*now[0][1]+now[0][1]*now[1][1])%1000000007],
            [(now[1][0]*now[0][0]+now[1][1]*now[1][0])%1000000007,(now[1][0]*now[0][1]+now[1][1]**2)%1000000007]
        ]
    cnt //= 2
    return conquer(now,divide(N-cnt))

N = int(input())

answer = divide(N//2)
start = [[0,1],[1,2]]
answer = conquer(start,answer)
if N%2==0:
    print(answer[0][0]%1000000007)
else:
    print(answer[0][1]%1000000007)