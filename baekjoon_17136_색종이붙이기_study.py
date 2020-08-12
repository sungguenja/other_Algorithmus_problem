paper = []
color = 0
for i in range(10):
    paper.append(list(map(int,input().split())))
    color += sum(paper[i])
visit = [[0]*10 for i in range(10)]
answer = 10*10
def solution(left,cnt=0,one=0,two=0,three=0,four=0,five=0):
    global answer
    if cnt>=answer:
        return
    
    if left == 0:
        if cnt<answer:
            answer = cnt
        return
    
    check = False
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 and visit[i][j] == 0:
                check = True
                break
        if check:
            break

    if check:
        if five<5:
            trigger = False
            for ni in range(i,i+5):
                for nj in range(j,j+5):
                    if ni>=10 or nj>=10 or paper[ni][nj] == 0 or visit[ni][nj] == 1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for ni in range(i,i+5):
                    for nj in range(j,j+5):
                        visit[ni][nj] = 1
                solution(left-25,cnt+1,one,two,three,four,five+1)
                for ni in range(i,i+5):
                    for nj in range(j,j+5):
                        visit[ni][nj] = 0
        if four<5:
            trigger = False
            for ni in range(i,i+4):
                for nj in range(j,j+4):
                    if ni>=10 or nj>=10 or paper[ni][nj] == 0 or visit[ni][nj] == 1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for ni in range(i,i+4):
                    for nj in range(j,j+4):
                        visit[ni][nj] = 1
                solution(left-16,cnt+1,one,two,three,four+1,five)
                for ni in range(i,i+4):
                    for nj in range(j,j+4):
                        visit[ni][nj] = 0
        if three<5:
            trigger = False
            for ni in range(i,i+3):
                for nj in range(j,j+3):
                    if ni>=10 or nj>=10 or paper[ni][nj] == 0 or visit[ni][nj] == 1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for ni in range(i,i+3):
                    for nj in range(j,j+3):
                        visit[ni][nj] = 1
                solution(left-9,cnt+1,one,two,three+1,four,five)
                for ni in range(i,i+3):
                    for nj in range(j,j+3):
                        visit[ni][nj] = 0
        if two<5:
            trigger = False
            for ni in range(i,i+2):
                for nj in range(j,j+2):
                    if ni>=10 or nj>=10 or paper[ni][nj] == 0 or visit[ni][nj] == 1:
                        trigger = True
                        break
                if trigger:
                    break
            else:
                for ni in range(i,i+2):
                    for nj in range(j,j+2):
                        visit[ni][nj] = 1
                solution(left-4,cnt+1,one,two+1,three,four,five)
                for ni in range(i,i+2):
                    for nj in range(j,j+2):
                        visit[ni][nj] = 0
        if one<5:
            visit[i][j] = 1
            solution(left-1,cnt+1,one+1,two,three,four,five)
            visit[i][j] = 0
solution(color)
if answer == 100:
    answer = -1
print(answer)