## pypy통과
N = int(input())
guilty = list(map(int,input().split()))
rate_change = [list(map(int,input().split())) for _ in range(N)]
eunjin = int(input())
answer = -1
visit = [0]*N
def solution(men,mafia,night=0,end=False):
    global answer
    if end or men==1:
        if night>answer:
            answer = night
        return
    
    if men & 1 == 0:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                for j in range(N):
                    if visit[j] == 0:
                        guilty[j] += rate_change[i][j]
                if i == mafia:
                    solution(men-1,mafia,night+1,True)
                else:
                    solution(men-1,mafia,night+1,False)
                for j in range(N):
                    if visit[j] == 0:
                        guilty[j] -= rate_change[i][j]
                visit[i] = 0
    else:
        trial = -1
        trial_guily = -80000
        for i in range(N):
            if visit[i] == 0 and guilty[i]>trial_guily:
                trial_guily = guilty[i]
                trial = i
        if trial == -1:
            return
        visit[trial] = 1
        if trial == mafia:
            solution(men-1,mafia,night,True)
        else:
            solution(men-1,mafia,night,False)
        visit[trial] = 0

solution(N,eunjin)
print(answer)