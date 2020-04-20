main_root = [list(range(0,41,2))]
main_root.append(list(range(10,20,3))+[25,30,35,40])
main_root.append([20,22,24,25,30,35,40])
main_root.append([30,28,27,26,25,30,35,40])


i=0
j=0
max_point=0
dice = list(map(int,input().split()))
for_visit = [0]*6
for i in range(10):
    for_visit[dice[i]] += 1
visit = [0]*6

def game(i=0,j=0,score=0,cnt=0):
    global max_point
    if cnt == 10:
        if max_point<score:
            max_point = score
        return
    
    for y in range(1,6):
        if visit[y] < for_visit[y]:
            visit[y] += 1
            if j+y>len(main_root[i]):
                game(0,0,score,10)
            elif i==0 and j+y==5:
                game(1,0,score+10,cnt+1)
            elif i==0 and j==10:
                game(2,0,score+20,cnt+1)
            elif i==0 and j==15:
                game(3,0,score+30,cnt+1)
            else:
                game(i,j+y,score+main_root[i][j+y],cnt+1)
            visit[y] -= 1
game()
print(max_point)
print(visit)
print(for_visit)