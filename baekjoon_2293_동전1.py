n,k=map(int,input().split())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
visit=[0]*(k+1)
for i in num_list:
    visit[i]+=1
    for j in range(i+1,len(visit)):
        visit[j] = visit[j-i]+visit[j]
print(visit[-1])