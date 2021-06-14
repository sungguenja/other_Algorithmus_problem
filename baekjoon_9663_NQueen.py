answer = 0
def checkQueen(array):
    i,j=array[-1]
    for k in range(1,N):
        lj = j - k
        rj = j + k
        ui = i - k
        di = i + k
        if lj<0 and lj>=N and rj<0 and rj>=N and ui<0 and ui>=N and di<0 and di>=N:
            break
        if 0<=lj<N and 0<=ui<N and visit[ui][lj]:
            return False
        if 0<=rj<N and 0<=ui<N and visit[ui][rj]:
            return False
        if 0<=rj<N and 0<=di<N and visit[di][rj]:
            return False
        if 0<=lj<N and 0<=di<N and visit[di][lj]:
            return False
    return True

def putQueen(goal,cnt=0,now=[]):
    global answer
    if not checkQueen(now):
        return

    if cnt == goal:
        answer += 1
        return

    for can in range(cnt*N,(cnt+1)*N):
        if not visit_i[case[can][0]] and not visit_j[case[can][1]] and not visit[case[can][0]][case[can][1]]:
            if case[can][1]>0:
                if case[can][1]<N-1:
                    if not visit[case[can][0]-1][case[can][1]] and not visit[case[can][0]-1][case[can][1]-1] and not visit[case[can][0]-1][case[can][1]+1]:
                        visit_i[case[can][0]] = True
                        visit_j[case[can][1]] = True
                        visit[case[can][0]][case[can][1]] = True
                        putQueen(goal,cnt+1,now+[case[can]])
                        visit_i[case[can][0]] = False
                        visit_j[case[can][1]] = False
                        visit[case[can][0]][case[can][1]] = False
                else:
                    if not visit[case[can][0]-1][case[can][1]] and not visit[case[can][0]-1][case[can][1]-1]:
                        visit_i[case[can][0]] = True
                        visit_j[case[can][1]] = True
                        visit[case[can][0]][case[can][1]] = True
                        putQueen(goal,cnt+1,now+[case[can]])
                        visit_i[case[can][0]] = False
                        visit_j[case[can][1]] = False
                        visit[case[can][0]][case[can][1]] = False
            else:
                if not visit[case[can][0]-1][case[can][1]] and not visit[case[can][0]-1][case[can][1]+1]:
                    visit_i[case[can][0]] = True
                    visit_j[case[can][1]] = True
                    visit[case[can][0]][case[can][1]] = True
                    putQueen(goal,cnt+1,now+[case[can]])
                    visit_i[case[can][0]] = False
                    visit_j[case[can][1]] = False
                    visit[case[can][0]][case[can][1]] = False

N = int(input())
case = [(i,j) for i in range(N) for j in range(N)]
visit_i = [False]*N
visit_j = [False]*N
visit = [[False]*N for i in range(N)]
for i in range(N):
    visit_i[0] = True
    visit_j[i] = True
    visit[0][i] = True
    putQueen(N,1,[(0,i)])
    visit_i[0] = False
    visit_j[i] = False
    visit[0][i] = False
print(answer)