N,M=map(int,input().split())
max_numb = 0
card = list(map(int,input().split()))
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if max_numb < card[i]+card[j]+card[k] <= M:
                max_numb = card[i]+card[j]+card[k]
print(max_numb)