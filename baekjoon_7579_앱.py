import sys
input = sys.stdin.readline
N,M = map(int,input().split())
app_list = [0] + list(map(int,input().split()))
cost_list = [0] + list(map(int,input().split()))
maximum_cost = sum(cost_list)
data_case = [[0]*(maximum_cost+1) for i in range(N+1)]
result = maximum_cost
if M != 0:
    for i in range(1,N+1):
        now_byte = app_list[i]
        now_cost = cost_list[i]
        for j in range(maximum_cost,-1,-1):
            if j - now_cost < 0:
                data_case[i][j] = data_case[i-1][j]
            else:
                data_case[i][j] = max(
                    now_byte + data_case[i-1][j-now_cost],
                    data_case[i-1][j]
                )
            
            if data_case[i][j] >= M:
                result = min(result,j)
    print(result)
else:
    print(0)