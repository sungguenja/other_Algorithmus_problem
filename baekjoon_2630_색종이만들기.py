count_0 = 0
count_1 = 0
def cutting(n,start_i,start_j):
    global count_0, count_1

    now = paper[start_i][start_j]

    for i in range(start_i,start_i+n):
        trigger = True
        for j in range(start_j,start_j+n):
            if now != paper[i][j]:
                trigger = False
                cutting(n//2,start_i,start_j)
                cutting(n//2,start_i,start_j+n//2)
                cutting(n//2,start_i+n//2,start_j)
                cutting(n//2,start_i+n//2,start_j+n//2)
                break
        if not trigger:
            break
    
    if trigger:
        if now == 1:
            count_1+=1
        else:
            count_0+=1


N=int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

cutting(N,0,0)
print(count_0)
print(count_1)