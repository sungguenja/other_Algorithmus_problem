N,M = map(int,input().split())
chess = [list(input()) for _ in range(N)]
a = 'BWBWBWBW'
b = 'WBWBWBWB'
answer = 8*8
for i in range(N-8+1):
    for j in range(M-8+1):
        answer_A = 0
        answer_B = 0
        trigger = True
        for ni in range(i,i+8):
            cnt = 0
            for nj in range(j,j+8):
                if trigger:
                    if chess[ni][nj] != a[cnt]:
                        answer_A += 1
                    if chess[ni][nj] != b[cnt]:
                        answer_B += 1
                else:
                    if chess[ni][nj] != b[cnt]:
                        answer_A += 1
                    if chess[ni][nj] != a[cnt]:
                        answer_B += 1
                cnt += 1
            trigger = not trigger
        answer = min(answer,answer_A,answer_B)
print(answer)