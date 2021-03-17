from copy import deepcopy
from collections import deque
N = int(input())
pipe = deque(map(int,input().split()))
hope = deque(map(int,input().split()))

answer = 0
answer_list = [0]*N
def lotto(pipe_list,hope_list):
    global answer,answer_list
    visit = [False]*N
    cnt = 0
    while pipe_list:
        check_head = pipe_list[0]
        check_tail = pipe_list[-1]
        for i in range(len(hope_list)):
            if visit[i] == False and hope_list[i] == check_head:
                visit[i] = True
                answer_list[cnt] = pipe_list.popleft()
                if answer_list[cnt] == hope_list[cnt]:
                    answer += 1
                cnt += 1
                break
            elif visit[i] == False and hope_list[i] == check_tail:
                visit[i] = True
                answer_list[cnt] = pipe_list.pop()
                if answer_list[cnt] == hope_list[cnt]:
                    answer += 1
                cnt += 1
                break
        
lotto(pipe,hope)
if answer == N:
    answer = 1
elif answer == N-1:
    answer = 2
elif answer == N-2:
    answer = 3
else:
    answer = "꽝"
answer_list = list(map(str,answer_list))
print(answer)
print(" ".join(answer_list))