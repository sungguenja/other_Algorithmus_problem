N,K = map(int,input().split())
checkpoint = []
answer = 0
for i in range(N):
    checkpoint.append(list(map(int,input().split())))
    answer += abs(checkpoint[i][0]) + abs(checkpoint[i][1])
def solution(now=0,jump=0,cost=0):
    global answer
    if cost>=answer:
        return
    
    if now==N-1:
        if cost<answer:
            answer = cost
        return
    
    if now+1<N:
        solution(now+1,jump,cost+abs(checkpoint[now+1][0]-checkpoint[now][0])+abs(checkpoint[now+1][1]-checkpoint[now][1]))
    
    if now+2<N and jump<K:
        solution(now+2,jump+1,cost+abs(checkpoint[now+2][0]-checkpoint[now][0])+abs(checkpoint[now+2][1]-checkpoint[now][1]))
solution()
print(answer)