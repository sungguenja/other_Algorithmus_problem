N,K = map(int,input().split())
# K+1은 해당 무게일 때 지금 최대 값어치
# N+1은 배낭에 넣는 물건들을 체크하는 상황
backpack = [[0]*(K+1) for i in range(N+1)]

values = [0]*(N+1)
weight = [0]*(N+1)

for i in range(N):
    W,V = map(int,input().split())
    values[i+1] = V
    weight[i+1] = W
    
def knapsack(items_weight_list,items_values_list,items_count,maximum_weight):
    for now_item in range(1,items_count+1):
        for now_weight in range(maximum_weight,-1,-1):
            # 지금 아이템 무게를 담을 수 있는가?
            if now_weight - items_weight_list[now_item] >= 0:
                backpack[now_item][now_weight] = max(
                    backpack[now_item-1][now_weight],
                    backpack[now_item-1][now_weight-items_weight_list[now_item]] + items_values_list[now_item]
                )
            else:
                backpack[now_item][now_weight] = backpack[now_item-1][now_weight]

    return max(backpack[now_item])

answer = knapsack(weight,values,N,K)
print(answer)