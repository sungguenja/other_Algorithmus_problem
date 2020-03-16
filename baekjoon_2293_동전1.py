n,k=map(int,input().split())
num_list=[]
for _ in range(n):
    num_list.append(int(input()))
visit=[0]*(k+1)
for i in num_list:
    if 0<=i<=k:
        visit[i]+=1
        for j in range(i+1,k+1):
            if 0<=j<=k and 0<=j-i<=k:
                visit[j] = visit[j-i]+visit[j]
print(visit[-1])