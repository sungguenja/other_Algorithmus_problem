def solution_1(n):
    answer = [[0],[0,0,1]]
    for i in range(2,n+1):
        b=[0]*len(answer[i-1])
        for j in range(len(answer[i-1])):
            if b[j] == answer[i-1][len(answer[i-1])-1-j]:
                b[j] = 1
        paper = answer[i-1] + [0] + b 
        answer.append(paper)
    return answer[n-1]

for i in range(1,4):
    print(solution_1(i))

memo = [[0]]
def solution_2(n):
    if len(memo) < n:
        for i in range(len(memo)-1,n-1):
            x = memo[i][::-1]
            for j in range(len(x)):
                if x[j] == 1:
                    x[j] = 0
                else:
                    x[j] = 1
            memo.append(memo[i]+[0]+x)
    return memo[n-1]

for i in range(1,4):
    print(solution_2(i))