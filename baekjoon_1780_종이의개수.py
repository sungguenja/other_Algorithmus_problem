count_0 = 0
count_1 = 0
count_2 = 0
def cutting(n,start_i,start_j):
    global count_0, count_1, count_2

    now = paper[start_i][start_j]

    for i in range(start_i,start_i+n):
        trigger = True
        for j in range(start_j,start_j+n):
            if now != paper[i][j]:
                trigger = False
                cutting(n//3,start_i,start_j)
                cutting(n//3,start_i,start_j+n//3)
                cutting(n//3,start_i,start_j+2*n//3)
                cutting(n//3,start_i+n//3,start_j)
                cutting(n//3,start_i+n//3,start_j+n//3)
                cutting(n//3,start_i+n//3,start_j+2*n//3)
                cutting(n//3,start_i+2*n//3,start_j)
                cutting(n//3,start_i+2*n//3,start_j+n//3)
                cutting(n//3,start_i+2*n//3,start_j+2*n//3)
                break
        if not trigger:
            break
    
    if trigger:
        if now == 1:
            count_1+=1
        elif now==0:
            count_0+=1
        else:
            count_2+=1

N=int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

cutting(N,0,0)
print(count_2)
print(count_0)
print(count_1)