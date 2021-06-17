N = int(input())
weights = list(map(int,input().split()))
K = int(input())
result_list = list(map(int,input().split()))
possible_list = []
backpack = [[0]*15001 for i in range(N+1)]

def knapsack(now,left,right):
    now_difference = abs(left-right)
    if now_difference not in possible_list:
        possible_list.append(now_difference)
    if now == N:
        return
    if backpack[now][now_difference] == 0:
        knapsack(now+1,left+weights[now],right)
        knapsack(now+1,left,right+weights[now])
        knapsack(now+1,left,right)
        backpack[now][now_difference] = 1

knapsack(0,0,0)
for result in result_list:
    if result in possible_list:
        print('Y',end=" ")
    else:
        print('N',end=" ")