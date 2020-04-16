def rotate(paper):
    r,c = len(paper),len(paper[0])
    return [[paper[r-1-j][i] for j in range(r)] for i in range(c)]

def posible(x,y):
    for i in range(len(paper)):
        for j in range(len(paper[i])):
            try:
                if note[y+i][x+j] == 1 and paper[i][j] == 1:
                    return False
            except IndexError:
                return False
    
    for i in range(len(paper)):
        for j in range(len(paper[i])):
            if paper[i][j] == 1:
                note[y+i][x+j] = 1
    
    return True

n,m,k = map(int,input().split())
note = [[0]*m for _ in range(n)]

for _ in range(k):
    r,c=map(int,input().split())
    paper = [list(map(int,input().split())) for _ in range(r)]
    trigger = False
    for k in range(4):
        for i in range(n-r+1):
            for j in range(m-c+1):
                if posible(j,i):
                    trigger = True
                    break
            if trigger:
                break
        if trigger:
            break
        paper = rotate(paper)
        r,c=c,r

cover = 0
for k in note:
    cover += sum(k)
print(cover)