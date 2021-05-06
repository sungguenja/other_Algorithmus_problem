class User:
    def __init__(self,language,job,carrer,food,point):
        self.language = language
        self.job = job
        self.carrer = carrer
        self.food = food
        self.point = int(point)
    
    def match(self,lang,job,carrer,food,point):
        if lang != '-' and self.language != lang:
            return False
        if job != '-' and self.job != job:
            return False
        if carrer != '-' and self.carrer != carrer:
            return False
        if food != '-' and self.food != food:
            return False
        if point != '-' and self.point < int(point):
            return False
        return True

def makeQuery(string):
    string = string.split()
    string = [string[0],string[2],string[4],string[6],string[7]]
    return string

def solution(info, query):
    answer = []
    for i in range(len(info)):
        people = info[i]
        lang,job,carrer,food,point = people.split()
        info[i] = User(lang,job,carrer,food,point)
    
    for i in range(len(query)):
        now_query = query[i]
        lang,job,carrer,food,point = makeQuery(now_query)
        cnt = 0
        for people in info:
            if people.match(lang,job,carrer,food,point):
                cnt += 1
        answer.append(cnt)

    return answer