import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

# A <-> F, B <-> D, C <-> E
class Dice:
    def __init__(self,arr):
        self.A = arr[0]
        self.B = arr[1]
        self.C = arr[2]
        self.D = arr[3]
        self.E = arr[4]
        self.F = arr[5]
        self.bottom = None
        self.top = None

N = int(input())
dice_list = []
for _ in range(N):
    dice_list.append(Dice(list(map(int,input().split()))))

answer = 0
def findAnswer(choiced,cnt=1):
    global answer
    if cnt == N:
        now_sum = 0
        for i in range(N):
            dice = dice_list[i]
            if choiced[i] == 0 or choiced[i] == 5:
                now_sum += max(dice.B,dice.C,dice.D,dice.E)
            elif choiced[i] == 1 or choiced[i] == 3:
                now_sum += max(dice.A,dice.C,dice.E,dice.F)
            elif choiced[i] == 2 or choiced[i] == 4:
                now_sum += max(dice.A,dice.B,dice.D,dice.F)
        if answer < now_sum:
            answer = now_sum
        return
    
    now_dice = dice_list[cnt]
    before_dice = dice_list[cnt-1]
    if choiced[cnt-1] == 0:
        if before_dice.F == now_dice.A:
            findAnswer(choiced+[0],cnt+1)
        if before_dice.F == now_dice.B:
            findAnswer(choiced+[1],cnt+1)
        if before_dice.F == now_dice.C:
            findAnswer(choiced+[2],cnt+1)
        if before_dice.F == now_dice.D:
            findAnswer(choiced+[3],cnt+1)
        if before_dice.F == now_dice.E:
            findAnswer(choiced+[4],cnt+1)
        if before_dice.F == now_dice.F:
            findAnswer(choiced+[5],cnt+1)
    elif choiced[cnt-1] == 1:
        if before_dice.D == now_dice.A:
            findAnswer(choiced+[0],cnt+1)
        if before_dice.D == now_dice.B:
            findAnswer(choiced+[1],cnt+1)
        if before_dice.D == now_dice.C:
            findAnswer(choiced+[2],cnt+1)
        if before_dice.D == now_dice.D:
            findAnswer(choiced+[3],cnt+1)
        if before_dice.D == now_dice.E:
            findAnswer(choiced+[4],cnt+1)
        if before_dice.D == now_dice.F:
            findAnswer(choiced+[5],cnt+1)
    elif choiced[cnt-1] == 2:
        if before_dice.E == now_dice.A:
            findAnswer(choiced+[0],cnt+1)
        if before_dice.E == now_dice.B:
            findAnswer(choiced+[1],cnt+1)
        if before_dice.E == now_dice.C:
            findAnswer(choiced+[2],cnt+1)
        if before_dice.E == now_dice.D:
            findAnswer(choiced+[3],cnt+1)
        if before_dice.E == now_dice.E:
            findAnswer(choiced+[4],cnt+1)
        if before_dice.E == now_dice.F:
            findAnswer(choiced+[5],cnt+1)
    elif choiced[cnt-1] == 3:
        if before_dice.B == now_dice.A:
            findAnswer(choiced+[0],cnt+1)
        if before_dice.B == now_dice.B:
            findAnswer(choiced+[1],cnt+1)
        if before_dice.B == now_dice.C:
            findAnswer(choiced+[2],cnt+1)
        if before_dice.B == now_dice.D:
            findAnswer(choiced+[3],cnt+1)
        if before_dice.B == now_dice.E:
            findAnswer(choiced+[4],cnt+1)
        if before_dice.B == now_dice.F:
            findAnswer(choiced+[5],cnt+1)
    elif choiced[cnt-1] == 4:
        if before_dice.C == now_dice.A:
            findAnswer(choiced+[0],cnt+1)
        if before_dice.C == now_dice.B:
            findAnswer(choiced+[1],cnt+1)
        if before_dice.C == now_dice.C:
            findAnswer(choiced+[2],cnt+1)
        if before_dice.C == now_dice.D:
            findAnswer(choiced+[3],cnt+1)
        if before_dice.C == now_dice.E:
            findAnswer(choiced+[4],cnt+1)
        if before_dice.C == now_dice.F:
            findAnswer(choiced+[5],cnt+1)
    elif choiced[cnt-1] == 5:
        if before_dice.A == now_dice.A:
            findAnswer(choiced+[0],cnt+1)
        if before_dice.A == now_dice.B:
            findAnswer(choiced+[1],cnt+1)
        if before_dice.A == now_dice.C:
            findAnswer(choiced+[2],cnt+1)
        if before_dice.A == now_dice.D:
            findAnswer(choiced+[3],cnt+1)
        if before_dice.A == now_dice.E:
            findAnswer(choiced+[4],cnt+1)
        if before_dice.A == now_dice.F:
            findAnswer(choiced+[5],cnt+1)

for i in range(6):
    findAnswer([i])

print(answer)