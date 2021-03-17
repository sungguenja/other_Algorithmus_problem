N,M = map(int,input().split())
set_price_list = [0]*M
one_price_list = [0]*M
for i in range(M):
    set_price,one_price = map(int,input().split())
    set_price_list[i] = set_price
    one_price_list[i] = one_price

answer = 0

def solution():
    global answer,set_price_list,one_price_list
    minimum_set_price_list = min(set_price_list)
    minimum_one_price_list = min(one_price_list)
    now_cost = min(minimum_one_price_list*4,minimum_set_price_list)
    answer += (N//4)*now_cost
    if N%4 != 0:
        answer += min(minimum_set_price_list,minimum_one_price_list*(N%4))
    print(answer)

solution()