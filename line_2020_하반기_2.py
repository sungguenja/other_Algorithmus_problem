from collections import deque
def solution(ball, order):
    answer = []
    ball = deque(ball)
    hold = []
    for i in range(len(order)):
        if ball[0] == order[i]:
            answer.append(ball.popleft())
            j = 0
            while j < len(hold):
                if hold[j] == ball[0]:
                    answer.append(ball.popleft())
                    hold.pop(j)
                    j=0
                elif hold[j] == ball[-1]:
                    answer.append(ball.pop())
                    hold.pop(j)
                    j=0
                else:
                    j+=1
        elif ball[-1] == order[i]:
            answer.append(ball.pop())
            j = 0
            while j < len(hold):
                if hold[j] == ball[0]:
                    answer.append(ball.popleft())
                    hold.pop(j)
                    j=0
                elif hold[j] == ball[-1]:
                    answer.append(ball.pop())
                    hold.pop(j)
                    j=0
                else:
                    j+=1
        else:
            hold.append(order[i])
    return answer