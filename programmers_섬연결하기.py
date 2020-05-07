# def solution(n, costs):
#     road = [0]*n
#     for root in costs:
#         if road[root[1]] == 0 or road[root[1]]>root[2]:
#             road[root[1]] = root[2]
#     return sum(road)

# def solution(n,costs):
#     bridge = set([costs[0][0]])
#     answer = 0
#     while len(bridge) < n:
#         price = 99999999
#         idx = 0
#         for i in range(len(costs)):
#             if costs[i][0] in bridge or costs[i][1] in bridge:
#                 if costs[i][0] in bridge and costs[i][1] in bridge:
#                     continue
#                 if price > costs[i][2]:
#                     price = costs[i][2]
#                     idx = i
#         answer += price
#         bridge.add(costs[idx][0])
#         bridge.add(costs[idx][1])
#     return answer

def solution(n,costs):
    visit = {0}
    answer = 0
    road = [[0]*n for _ in range(n)]
    for root in costs:
        road[root[0]][root[1]] = root[2]

    while len(visit) != n:
        price = 99999999
        where_j = 0
        for i in visit:
            for j in range(n):
                if road[i][j] != 0 and price>road[i][j]:
                    price = road[i][j]
                    where_i = i
                    where_j = j
        if where_i in visit and where_j in visit:
            road[where_i][where_j] = 0
        else:
            visit.add(where_i)
            visit.add(where_j)
            road[where_i][where_j] = 0
            answer+=price
    return answer
                

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))