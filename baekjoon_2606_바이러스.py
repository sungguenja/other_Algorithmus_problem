def virus(N,start=1):
    visit[start] = 1

    for i in range(N+1):
        if visit[i] == 0 and computer[start][i] == 1:
            virus(N,i)


N=int(input())

computer = [[0]*(N+1) for _ in range(N+1)]

for _ in range(int(input())):
    start,end=map(int,input().split())
    computer[start][end] = 1
    computer[end][start] = 1

visit=[0]*(N+1)
virus(N)
print(visit.count(1)-1)