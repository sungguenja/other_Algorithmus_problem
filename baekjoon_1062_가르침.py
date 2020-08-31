N,K = map(int,input().split())
word_list = [set(input()) for i in range(N)]
learn = [False for i in range(26)]
for i in ['a','c','i','n','t']:
    learn[ord(i)-ord('a')] = True
answer = 0
def solution(idx=0,cnt=0):
    global answer
    if cnt == K-5:
        amount = 0
        for word in word_list:
            for alphabet in word:
                if not learn[ord(alphabet)-ord('a')]:
                    break
            else:
                amount += 1
        if answer<amount:
            answer = amount
        return
    else:
        for i in range(idx,26):
            if not learn[i]:
                learn[i] = True
                solution(i,cnt+1)
                learn[i] = False
if K<5:
    answer = 0
elif K==26:
    answer = N
else:
    solution()
print(answer)