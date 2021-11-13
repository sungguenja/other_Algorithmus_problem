class Person:
    def __init__(self,status):
        benefit,delivery = status
        self.benefit = benefit
        self.delivery = delivery

N = int(input())
person_list = [Person(map(int,input().split())) for i in range(N)]

maximum_benefit = 0
result = 0
for i in range(N):
    now_benefit = 0
    now_price = person_list[i].benefit
    for j in range(N):
        if now_price <= person_list[j].benefit and now_price >= person_list[j].delivery:
            now_benefit += now_price - person_list[j].delivery
    if maximum_benefit < now_benefit:
        maximum_benefit = now_benefit
        result = now_price
    elif maximum_benefit == now_benefit:
        result = min(result,now_price)

print(result)