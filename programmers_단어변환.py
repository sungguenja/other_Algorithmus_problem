def solution(begin, target, words):
    answer = 0
    stack = [[begin,0]]
    visit = [0]*len(words)
    while stack != []:
        now,cnt = stack.pop()
        if now == target:
            if answer == 0 or answer>cnt:
                answer = cnt
            continue
        for i in range(len(words)):
            cnt_now = 0
            for j in range(len(words[i])):
                if now[j] != words[i][j]:
                    cnt_now+=1
            else:
                if cnt_now == 1 and visit[i] < len(words):
                    visit[i] += 1
                    stack.append([words[i],cnt+1])
    return answer

print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))