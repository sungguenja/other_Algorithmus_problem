from copy import deepcopy
class Furniture:
    def __init__(self,name,buyer_list,cnt):
        self.name = name
        self.buyer_list = buyer_list
        self.cnt = cnt

class People:
    def __init__(self,name,want_list,cnt):
        self.name = name
        self.want_list = want_list
        self.cnt = 0
        self.maximum = cnt
    
    def __str__(self):
        return "{0} {1} {2}".format(self.name,self.cnt,self.want_list)

N = int(input())
furniture_list = [0]*N
for i in range(N):
    name,buyer,cnt = input().split()
    furniture = Furniture(name,list(buyer),int(cnt))
    furniture_list[i] = furniture

M = int(input())
people_list = [0]*M
for i in range(M):
    name,buyer,cnt = input().split()
    buyer = list(buyer)
    cnt = int(cnt)
    people_list[i] = People(name,buyer[:cnt],cnt)

nnn = 0
chosen_list = [[] for i in range(N)]
before_list = []
while not isSame(chosen_list,before_list):
    nnn += 1
    before_list = deepcopy(chosen_list)
    for people in people_list:
        if people.cnt >= people.maximum:
            continue
        want = people.want_list[people.cnt]
        target = N
        for i in range(N):
            if furniture_list[i].name == want:
                target = i
                break
        if len(chosen_list[target]) < furniture_list[target].cnt:
            for j in range(M):
                if furniture_list[target].buyer_list[j] == people.name:
                    chosen_list[target].append((people,j))
                    break
        else:
            buyer_rank = M+1
            for j in range(M):
                if furniture_list[target].buyer_list[j] == people.name:
                    buyer_rank = j
                    break
            change_target = len(chosen_list[target])
            change_target_rank = buyer_rank
            trigger = True
            for i in range(len(chosen_list[target])):
                if chosen_list[target][i][0].name == people.name:
                    trigger = False
                    break
                if chosen_list[target][i][1] > change_target_rank:
                    change_target = i
                    change_target_rank = chosen_list[target][i][1]
            if trigger:
                if change_target < len(chosen_list[target]):
                    chosen_list[target][change_target] = (people,buyer_rank)
                else:
                    people.cnt += 1
    
def isSame(chosen_list,before_list):
    if len(chosen_list) != len(before_list):
        return False
    
    for i in range(len(chosen_list)):
        if len(chosen_list[i]) != len(before_list[i]):
            return False
        for j in range(len(chosen_list[i])):
            if type(chosen_list[i][j]) != type(before_list[i][j]):
                return False
            else:
                if type(chosen_list[i][j][0]) == People: