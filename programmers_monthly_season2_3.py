def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    for i in a:
        if i>0:
            answer += i
    N = len(edges)
    answer = (answer**2)*N
    visit = [False]*N
    def innerSolution(weights,cost):
        nonlocal answer
        if cost >= answer:
            return
        trigger = False

        for weight in weights:
            if weight != 0:
                trigger = True
                break

        if not trigger:
            if cost < answer:
                answer = cost
            return

        for i in range(N):
            if visit[i] == False:
                visit[i] = True
                start = edges[i][0]
                goal = edges[i][1]
                save_weights = weights[:]
                now_weights = save_weights[:]
                next_cost_start = save_weights[start]
                next_cost_goal = save_weights[goal]
                if next_cost_goal != 0:
                    now_weights[start] += next_cost_goal
                    now_weights[goal] = 0
                    innerSolution(now_weights[:],cost+abs(next_cost_goal))
                now_weights = save_weights[:]
                if next_cost_start != 0:
                    now_weights[goal] += next_cost_start
                    now_weights[start] = 0
                    innerSolution(now_weights[:],cost+abs(next_cost_start))
                visit[i] = False
    innerSolution(a,0)
    return answer