N,K = map(int,input().split())
student = [0]*N
word = [0]*21 # 0~20 글자수
answer = 0
for rank in range(N):
    now = len(input())
    student[rank] = now
    if rank>K:
        word[student[rank-K-1]] -= 1 # K 범위 밖
    answer += word[now]
    word[now] += 1
print(answer)