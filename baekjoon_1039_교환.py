from collections import deque
number,N = input().split()
N = int(N)
length = len(number)
visit = {}
trigger = False
for i in number:
    if visit.get(i) == None:
        visit[i] = 1
    else:
        trigger = True
        break

answer = -1
visit = {}
def solution(now,K,length):
    global answer
    Que = deque()
    Que.append((now,0))
    while Que:
        check,cnt = Que.popleft()
        if cnt == K:
            now_answer = int(check)
            if check[0] != 0 and answer < now_answer:
                answer = now_answer
            continue
        
        if (K-cnt)%2 == 0 or trigger:
            now_answer = int(check)
            if check[0] != 0 and answer < now_answer:
                answer = now_answer

        for i in range(length-1):
            for j in range(i+1,length):
                if i == 0  and check[j] == '0' :
                    continue
                next_arr = check
                next_arr = next_arr[:i] + check[j] + next_arr[i+1:j] + check[i] + next_arr[j+1:]
                if visit.get(next_arr) == None:
                    visit[next_arr] = cnt + 1
                    Que.append((next_arr,cnt+1))
if length > 2:
    solution(number,N,length)
elif length == 2:
    if number[1] != '0':
        solution(number,N,length)
print(answer)