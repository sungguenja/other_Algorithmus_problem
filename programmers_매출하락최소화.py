import sys
sys.setrecursionlimit(9999)
class Worker:
    def __init__(self,number,sale):
        self.number = number
        self.sale = sale
        self.team_leader = None
        self.team_number = 0
        self.member = []

    def addMember(self,member):
        self.member.append(member)

    def mateTeamLeader(self,leader):
        self.team_leader = leader

    def findTeamNumber(self,number):
        self.team_number = number

    def findTeam(self):
        self.team_number = self.team_leader.team_number
        return self.team_number

    def hasTeam(self):
        return not (len(self.member) == 0)

answer = 2**31

def findMinimumCost(now,cost,team_list,end,visit=[]):
    global answer
    if cost>=answer:
        return

    if now == end:
        if answer > cost:
            answer = cost
        return
    
    check_team = team_list[now]
    trigger = False
    for vi in visit:
        if vi in check_team:
            trigger = True
    if trigger:
        findMinimumCost(now+1,cost,team_list,end,visit)
        for worker in check_team:
            findMinimumCost(now+1,cost+worker.sale,team_list,end,visit+[worker])
    else:
        for worker in check_team:
            findMinimumCost(now+1,cost+worker.sale,team_list,end,visit+[worker])

def solution(sales, links):
    global answer
    company = [0]
    for i in range(len(sales)):
        company.append(Worker(i+1,sales[i]))

    for i in range(len(links)):
        leader,member = links[i]
        company[leader].addMember(company[member])
        company[member].mateTeamLeader(company[leader])
        
    team = {}
    cnt = 1
    for worker in company:
        if worker == 0:
            continue
        if worker.hasTeam():
            team[cnt] = [worker]
            worker.findTeamNumber(cnt)
            for coworker in worker.member:
                team[cnt].append(coworker)
            cnt += 1

    findMinimumCost(1,0,team,cnt)
    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))