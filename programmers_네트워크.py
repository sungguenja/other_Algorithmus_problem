def solution(n, computers):
    answer = []
    for i in range(n):
        visit = [0]*n
        stack = [i]
        while stack != []:
            x = stack.pop()
            for z in range(n):
                if computers[x][z]==1 and visit[z] == 0:
                    visit[z]=1
                    stack.append(z)
        if visit not in answer:
            answer.append(visit)
    return len(answer)

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))
print(solution(3,[[1,1,0],[1,1,1],[0,1,1]]))