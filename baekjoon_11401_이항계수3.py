N,K = map(int,input().split())
answer = 1
if N-K<=K:
    for i in range(N,K,-1):
        answer *= i
    for i in range(N-K,0,-1):
        answer //= i
else:
    for i in range(N,N-K,-1):
        answer *= i
    for i in range(K,0,-1):
        answer //= i

print(answer)