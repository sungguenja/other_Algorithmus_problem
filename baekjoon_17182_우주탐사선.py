answer = 0

def solution(N,whe,cost=0):
    global answer
    if cost>=answer:
        return
    
    if 0 not in visit:
        if answer>cost:
            answer = cost
        return
    
    for i in range(N):
        if i != whe and visit[i]<N-1:
            visit[i] += 1
            solution(N,i,cost+planet[whe][i])
            visit[i] -= 1

N,start = map(int,input().split())
planet = [0]*N
for i in range(N):
    minimum = 1001
    planet[i] = list(map(int,input().split()))
    for j in range(N):
        if planet[i][j] != 0 and minimum>planet[i][j]:
            minimum = planet[i][j]
    answer += minimum*N
visit = [0]*N
visit[start] = 1
solution(N,start)
print(answer)
# 플로이드 와샬인 듯 하다.....
# 플로이드 와샬을 익히고 풀어보자