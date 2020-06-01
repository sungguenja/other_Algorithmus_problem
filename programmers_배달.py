def solution(N, road, K):
    answer = 0
    guide = [[-1]*(N+1) for _ in range(N+1)]
    for rod in road:
        if guide[rod[0]][rod[1]] == -1 and guide[rod[1]][rod[0]] == -1:
            guide[rod[0]][rod[1]], guide[rod[1]][rod[0]] = rod[2], rod[2]
        else:
            if rod[2]<guide[rod[0]][rod[1]]:
                guide[rod[0]][rod[1]], guide[rod[1]][rod[0]] = rod[2], rod[2]
    visit = [9999999]*(N+1)
    Que = [1]
    visit[1] = 0
    while Que != []:
        now = Que.pop(0)
        for i in range(1,N+1):
            if guide[now][i] != -1:
                if visit[i] > visit[now] + guide[now][i] and visit[now] + guide[now][i] <= K:
                    visit[i] = visit[now] + guide[now][i]
                    Que.append(i)
    for i in range(N+1):
        if -1<visit[i]<=K:
            answer+=1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))