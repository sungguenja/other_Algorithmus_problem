N,K = map(int,input().split())
answer = 1
p = 1000000007

factorial = [0]*(N+1)
factorial[1] = 1
for i in range(2,N+1):
    factorial[i] = i*factorial[i-1]%p

answer = factorial[N]%p
B = (factorial[N-K]*factorial[K])%p

def multiple(a,b):
    if b==0:
        return 1
    if b%2 == 1:
        return (multiple(a,b//2)**2*a)%p
    else:
        return (multiple(a,b//2)**2)%p

answer = (answer*(multiple(B,p-2)%p))%p

print(answer)