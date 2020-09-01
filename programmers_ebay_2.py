import sys
sys.setrecursionlimit(5000)
def solution(num, cards):
    answer = 0
    for i in range(len(cards)):
        if num%cards[i]==0:
            if answer == 0 or answer>num%cards[i]:
                answer = num%cards[i]
    if answer == 0:
        answer = num
    def sol(now=0,cost=0,cnt=0):
        nonlocal answer
        if cnt >= answer or cost > num:
            return
        if cost == num:
            if cnt<answer:
                answer = cnt
            return
        for i in range(now,len(cards)):
            sol(i,cost+cards[i],cnt+1)
    if answer != 1 or answer != 2:
        sol()
    if answer == num:
        answer = -1
    return answer