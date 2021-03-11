from collections import deque
N = int(input())

def makeOne(number):
    answer = 0
    visit = [False]*(number+1)
    history = [-1]*(number+1)
    Que = deque()
    history[number] = -2
    Que.append((number,0))
    while Que:
        now_queue_data = Que.popleft()
        now_number,now_cnt = now_queue_data[0],now_queue_data[1]
        if now_number == 1:
            if answer == 0 or answer > now_cnt:
                answer = now_cnt
            continue

        if now_number%3 == 0:
            if not visit[now_number//3]:
                visit[now_number//3] = True
                history[now_number//3] = now_number
                Que.append((now_number//3,now_cnt+1))
        if now_number%2 == 0:
            if not visit[now_number//2]:
                visit[now_number//2] = True
                history[now_number//2] = now_number
                Que.append((now_number//2,now_cnt+1))
        if now_number > 1:
            if not visit[now_number-1]:
                visit[now_number-1] = True
                history[now_number-1] = now_number
                Que.append((now_number-1,now_cnt+1))
    print(answer)

    print_history = ['1']
    now_number = 1
    while history[now_number] != -2:
        now_number = history[now_number]
        print_history.append(str(now_number))
    print_history = print_history[::-1]
    print(' '.join(print_history))
makeOne(N)