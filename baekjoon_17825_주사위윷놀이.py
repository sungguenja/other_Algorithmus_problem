main_root = [list(range(0,41,2))]
main_root.append(list(range(10,20,3))+[25,30,35,40])
main_root.append([20,22,24,25,30,35,40])
main_root.append([30,28,27,26,25,30,35,40])

i=0
j=0
max_point=0
dice = list(map(int,input().split()))
visit = [0]*6
for i in range(10):
    visit[dice[i]] += 1

def game(a_i=0,a_j=0,b_i=0,b_j=0,c_i=0,c_j=0,d_i=0,d_j=0,score=0):
    global max_point
    if visit == [0]*6 and max_point<score:
        max_point=score
        return
    
    for i in range(1,6):
        if visit[i]>0:
            if a_i != None
                if a_j+i<len(main_root[a_i]):
                    if main_root[a_i][a_j+i] == 10:
                        visit[i]-=1
                        game(1,0,b_i,b_j,c_i,c_j,d_i,d_j,score+10)
                        visit[i]+=1
                    elif main_root[a_i][a_j+i] == 20:
                        visit[i]-=1
                        game(2,0,b_i,b_j,c_i,c_j,d_i,d_j,score+20)
                        visit[i]+=1
                    elif main_root[a_i][a_j+i] == 30:
                        visit[i]-=1
                        game(3,0,b_i,b_j,c_i,c_j,d_i,d_j,score+30)
                        visit[i]+=1
                    else:
                        visit[i]-=1
                        game(a_i,a_j+i,b_i,b_j,c_i,c_j,d_i,d_j,score+main_root[a_i][a_j+i])
                        visit[i]+=1
                else:
                    game(None,None,b_i,b_j,c_i,c_j,d_i,d_j,score)
            elif b_i != None
                if b_j+i<len(main_root[b_i]):
                    if main_root[b_i][b_j+i] == 10:
                        visit[i]-=1
                        game(a_i,a_j,1,0,c_i,c_j,d_i,d_j,score+10)
                        visit[i]+=1
                    elif main_root[b_i][b_j+i] == 20:
                        visit[i]-=1
                        game(a_i,a_j,2,0,c_i,c_j,d_i,d_j,score+20)
                        visit[i]+=1
                    elif main_root[b_i][b_j+i] == 30:
                        visit[i]-=1
                        game(a_i,a_j,3,0,c_i,c_j,d_i,d_j,score+30)
                        visit[i]+=1
                    else:
                        visit[i]-=1
                        game(a_i,a_j,b_i,b_j+i,c_i,c_j,d_i,d_j,score+main_root[b_i][b_j+i])
                        visit[i]+=1
                else:
                    game(a_i,a_j,None,None,c_i,c_j,d_i,d_j,score)
            elif b_i != None
                if b_j+i<len(main_root[b_i]):
                    if main_root[b_i][b_j+i] == 10:
                        visit[i]-=1
                        game(a_i,a_j,1,0,c_i,c_j,d_i,d_j,score+10)
                        visit[i]+=1
                    elif main_root[b_i][b_j+i] == 20:
                        visit[i]-=1
                        game(a_i,a_j,2,0,c_i,c_j,d_i,d_j,score+20)
                        visit[i]+=1
                    elif main_root[b_i][b_j+i] == 30:
                        visit[i]-=1
                        game(a_i,a_j,3,0,c_i,c_j,d_i,d_j,score+30)
                        visit[i]+=1
                    else:
                        visit[i]-=1
                        game(a_i,a_j,b_i,b_j+i,c_i,c_j,d_i,d_j,score+main_root[b_i][b_j+i])
                        visit[i]+=1
                else:
                    game(a_i,a_j,None,None,c_i,c_j,d_i,d_j,score)

# 머 대충 이렇게 하면 될 듯 너무 귀찮다
game()
print(max_point)