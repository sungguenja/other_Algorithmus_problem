answer = 0
paper = [list(map(int,input().split())) for _ in range(10)]
for k in paper:
    answer += sum(k)
ans = answer
visit = [[0]*10 for _ in range(10)]
answer += 1
save_answer = answer 
def solution(cnt=0,a=0,b=0,c=0,d=0,e=0):
    global answer

    if a+b+c+d+e>=answer or a>=6 or b>=6 or c>=6 or d>=6 or e>=6:
        return
    
    if cnt == ans:
        if a+b+c+d+e<answer:
            answer = a+b+c+d+e
        return
    
    check_trigger = False
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 and visit[i][j] == 0:
                check_trigger = True
                break
        if check_trigger:
            break
    
    if check_trigger:
        if e<5:
            trigger = False
            for y in range(i,i+5):
                for x in range(j,j+5):
                    if y>=10 or x>=10 or paper[y][x]==0 or visit[y][x]==1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for y in range(i,i+5):
                    for x in range(j,j+5):
                        visit[y][x] = 1
                solution(cnt+25,a,b,c,d,e+1)
                for y in range(i,i+5):
                    for x in range(j,j+5):
                        visit[y][x] = 0
        
        if d<5:
            trigger = False
            for y in range(i,i+4):
                for x in range(j,j+4):
                    if y>=10 or x>=10 or paper[y][x]==0 or visit[y][x]==1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for y in range(i,i+4):
                    for x in range(j,j+4):
                        visit[y][x] = 1
                solution(cnt+16,a,b,c,d+1,e)
                for y in range(i,i+4):
                    for x in range(j,j+4):
                        visit[y][x] = 0
        
        if c<5:
            trigger = False
            for y in range(i,i+3):
                for x in range(j,j+3):
                    if y>=10 or x>=10 or paper[y][x]==0 or visit[y][x]==1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for y in range(i,i+3):
                    for x in range(j,j+3):
                        visit[y][x] = 1
                solution(cnt+9,a,b,c+1,d,e)
                for y in range(i,i+3):
                    for x in range(j,j+3):
                        visit[y][x] = 0
        
        if b<5:
            trigger = False
            for y in range(i,i+2):
                for x in range(j,j+2):
                    if y>=10 or x>=10 or paper[y][x]==0 or visit[y][x]==1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for y in range(i,i+2):
                    for x in range(j,j+2):
                        visit[y][x] = 1
                solution(cnt+4,a,b+1,c,d,e)
                for y in range(i,i+2):
                    for x in range(j,j+2):
                        visit[y][x] = 0
        
        if a<5:
            trigger = False
            for y in range(i,i+1):
                for x in range(j,j+1):
                    if y>=10 or x>=10 or paper[y][x]==0 or visit[y][x]==1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for y in range(i,i+1):
                    for x in range(j,j+1):
                        visit[y][x] = 1
                solution(cnt+1,a+1,b,c,d,e)
                for y in range(i,i+1):
                    for x in range(j,j+1):
                        visit[y][x] = 0

solution()
if answer == save_answer:
    answer = -1
print(answer)