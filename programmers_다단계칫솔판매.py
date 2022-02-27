class Recommender:
    def __init__(self,name):
        self.name = name
        self.my_recommender = None
        self.amount = 0
        self.recommendee_cost = 0
        self.benefit = 0
        
    def giveRecommendCost(self,cost):
        fee = int(cost*0.1)
        self.recommendee_cost += cost - fee
        if self.my_recommender != None and fee >= 1:
            self.my_recommender.giveRecommendCost(fee)
        
    def setMyRecommedeeCost(self):
        fee = int(self.amount*0.1)
        self.benefit += self.amount - fee
        if self.my_recommender != None and fee >= 1:
            self.my_recommender.giveRecommendCost(fee)
    
    def setAmount(self,amount):
        self.amount = amount
        
def solution(enroll, referral, seller, amount):
    people = {}
    for enroll_person in enroll:
        people[enroll_person] = Recommender(enroll_person)
    
    for i in range(len(referral)):
        recommender_name = referral[i]
        recommendee_name = enroll[i]
        if recommender_name != '-':
            people[recommendee_name].my_recommender = people[recommender_name]
    
    for i in range(len(seller)):
        person = seller[i]
        now_amount = amount[i]
        people[person].setAmount(now_amount*100)
        people[person].setMyRecommedeeCost()
        
    answer = []
    for key,value in people.items():
        answer.append(value.recommendee_cost+value.benefit)
    
    return answer