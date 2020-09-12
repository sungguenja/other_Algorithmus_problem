def solution(sales, links):
    answer = sum(sales)
    department = {}
    visit = [0]*len(sales)
    visit_department = {}
    for i in links:
        if department.get(i[0]-1)== None:
            department[i[0]-1] = [i[0]-1,i[1]-1]
            visit_department[i[0]-1] = 0
        else:
            department[i[0]-1].append(i[1]-1)
    def dfs(N,whe=-1,cost=0):
        nonlocal answer
        if cost>=answer:
            return
        for j in visit_department.keys():
            if visit_department[j] == 0:
                break
        else:
            if cost<answer:
                answer = cost
            return
        for j in range(whe+1,N):
            if visit[j] == 0:
                visit[j] = 1
                for k in visit_department.keys():
                    if j in department[k]:
                        visit_department[k] += 1
                dfs(N,j,cost+sales[j])
                visit[j] = 0
                for k in visit_department.keys():
                    if j in department[k]:
                        visit_department[k] -= 1

    dfs(len(sales),-1,0)
    return answer