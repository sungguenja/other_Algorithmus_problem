def knapsack(goal,item_list,length,now_sum):
    global result_answer
    if length == 0 or goal > now_sum or result_answer == 'Y':
        return 
    backpack = [[0]*(goal+1) for i in range(length)]

    for now_item in range(length):
        for now_weight in range(goal,-1,-1):
            if now_weight - item_list[now_item] >= 0:
                backpack[now_item][now_weight] = max(
                    backpack[now_item-1][now_weight],
                    backpack[now_item-1][now_weight - item_list[now_item]] + item_list[now_item]
                )
            else:
                backpack[now_item][now_weight] = backpack[now_item-1][now_weight]

    if backpack[-1][-1] == goal:
        result_answer = 'Y'
        return 
    else:
        backpack = None
        next_sum = sum(item_list)
        for now_item in range(length):
            next_sum -= item_list[now_item]
            if goal + item_list[now_item] < next_sum:
                knapsack(goal+item_list[now_item],item_list[:now_item] + item_list[now_item+1:],length-1,next_sum)
                if result_answer == 'Y':
                    return
            elif goal + item_list[now_item] == next_sum:
                result_answer = 'Y'
                return
            next_sum += item_list[now_item]

N = int(input())
weights = list(map(int,input().split()))
K = int(input())
result = list(map(int,input().split()))
answer = []
for result_item in result:
    result_answer = 'N'
    knapsack(result_item,weights,N,sum(weights))
    answer.append(result_answer)

print(" ".join(answer))