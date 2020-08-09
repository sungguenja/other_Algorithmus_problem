answer = 0
def healchang(n,k,now=500):
    global answer
    if now<500:
        return
    
    if visit == [1]*n:
        answer += 1
        return
    
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            healchang(n,k,now-k+physical[i])
            visit[i] = 0
N,K = map(int,input().split())
physical = list(map(int,input().split()))
visit = [0]*N
healchang(N,K)
print(answer)