def solution(n, z, roads, queries):
    answer = []
    road_length = len(roads)
    now_answer = 0
    memo = {}
    def innerSolution(cost,remaining,start):
        nonlocal now_answer
        
        if cost >= now_answer:
            memo[remaining] = 999999
            return

        if memo.get(remaining) != None:
            if cost + memo.get(remaining) < now_answer:
                now_answer = cost + memo.get(remaining)
            return

        if remaining%z == 0:

            if memo.get(remaining) == None or memo.get(remaining) < cost + remaining//z:
                memo[remaining] = cost + remaining//z

            if cost + remaining//z < now_answer:
                now_answer = cost + remaining//z
            return
        
        
    for query in queries:
        visit = [False]*road_length
        now_answer = 0
        if query % z == 0:
            now_answer = query//z
        else:
            now_answer = (query//z + 10)*2
            innerSolution(0,query,0)
            if now_answer == (query//z + 10)*2:
                now_answer = -1
        answer.append(now_answer)
    return answer