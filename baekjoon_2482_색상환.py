N = int(input())
K = int(input())
MOD_NUMBER = 1000000003
color_choice_cnt_list = [[0]*(K+1) for i in range(N+1)]
for i in range(N+1):
    color_choice_cnt_list[i][1] = i
    color_choice_cnt_list[i][0] = 0

for i in range(2,N+1):
    for j in range(2,K+1):
        color_choice_cnt_list[i][j] = (color_choice_cnt_list[i-1][j] + color_choice_cnt_list[i-2][j-1]) % MOD_NUMBER

if K == 1:
    print(N)
else:
    print((color_choice_cnt_list[N-1][K]+color_choice_cnt_list[N-3][K-1])%MOD_NUMBER)