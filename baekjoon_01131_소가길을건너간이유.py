C,N=map(int,input().split())

chicken = [None]*C
cow = [None]*N

for i in range(C):
    chicken[i] = int(input())

chicken.sort()

for i in range(N):
    cow[i] = list(map(int,input().split()))
    cow[i][0],cow[i][1] = cow[i][1],cow[i][0]

cow.sort()
answer = 0
cow_visit = [None]*N
for i in range(C):
    for j in range(N):
        if cow_visit[j]==None and cow[j][1]<=chicken[i]<=cow[j][0]:
            answer+=1
            cow_visit[j] = 1
            break

print(answer)