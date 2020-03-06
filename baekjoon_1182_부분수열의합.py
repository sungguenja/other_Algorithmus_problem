N,final=map(int,input().split())
num_list=list(map(int,input().split()))
cnt=0
for i in range(1,1<<N):
    su=0
    for j in range(N):
        if i&(1<<j):
            su+=num_list[j]
    if su==final:
        cnt+=1
print(cnt)