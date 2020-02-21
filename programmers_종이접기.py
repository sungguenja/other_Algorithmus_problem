def solution(n):
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
    print(solution(i))