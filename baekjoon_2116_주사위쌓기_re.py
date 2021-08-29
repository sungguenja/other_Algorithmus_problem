import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(20000)

# A0 <-> F5, B1 <-> D3, C2 <-> E4
N = int(input())
dice_list = [list(map(int,input().split())) for i in range(N)]
answer = 0

def bfs(first):
    global answer
    Que = deque()
    for i in range(6):
        check = 0
        if i == 0 or i == 5:
            check = max(first[1],first[2],first[3],first[4])
        elif i == 1 or i == 3:
            check = max(first[0],first[2],first[4],first[5])
        elif i == 2 or i == 4:
            check = max(first[0],first[1],first[3],first[5])
        Que.append((1,i,check))
    
    while Que:
        cnt,bottom,now_sum = Que.popleft()
        if cnt == N:
            if answer < now_sum:
                answer = now_sum
            continue

        now_dice = dice_list[cnt]
        before_dice = dice_list[cnt-1]

        if bottom == 0:
            if before_dice[4] == now_dice[0]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
            if before_dice[4] == now_dice[1]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[4] == now_dice[2]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[4] == now_dice[3]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[4] == now_dice[4]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[4] == now_dice[5]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
        elif bottom == 1:
            if before_dice[3] == now_dice[0]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
            if before_dice[3] == now_dice[1]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[3] == now_dice[2]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[3] == now_dice[3]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[3] == now_dice[4]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[3] == now_dice[5]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
        elif bottom == 2:
            if before_dice[4] == now_dice[0]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
            if before_dice[4] == now_dice[1]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[4] == now_dice[2]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[4] == now_dice[3]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[4] == now_dice[4]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[4] == now_dice[5]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
        elif bottom == 3:
            if before_dice[1] == now_dice[0]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
            if before_dice[1] == now_dice[1]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[1] == now_dice[2]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[1] == now_dice[3]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[1] == now_dice[4]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[1] == now_dice[5]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
        elif bottom == 4:
            if before_dice[2] == now_dice[0]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
            if before_dice[2] == now_dice[1]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[2] == now_dice[2]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[2] == now_dice[3]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[2] == now_dice[4]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[2] == now_dice[5]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
        elif bottom == 5:
            if before_dice[0] == now_dice[0]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))
            if before_dice[0] == now_dice[1]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[0] == now_dice[2]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[0] == now_dice[3]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[2],now_dice[5],now_dice[4])))
            if before_dice[0] == now_dice[4]:
                Que.append((cnt+1,0,now_sum+max(now_dice[0],now_dice[1],now_dice[5],now_dice[3])))
            if before_dice[0] == now_dice[5]:
                Que.append((cnt+1,0,now_sum+max(now_dice[1],now_dice[2],now_dice[3],now_dice[4])))

bfs(dice_list[0])
print(answer)