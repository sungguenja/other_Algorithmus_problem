answer = []
def dfs(start,):
    pass
def solution(tickets):
    global answer
    road = dict()
    visit = dict()
    for ticket in tickets:
        if road.get(ticket[0]) == None:
            road[ticket[0]] = [ticket[1]]
            visit[ticket[0]] = [0]
        else:
            road[ticket[0]].append(ticket[1])
            visit[ticket[0]].append(0)
            road[ticket[0]].sort(reverse=True)
    print(road)
    return answer

print(solution([ [ 'ICN', 'BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], [ 'DOO', 'COO' ], [ 'BOO', 'DOO' ],[ 'DOO', 'BOO' ], [ 'BOO', 'ICN' ], [ 'COO', 'BOO' ] ] ))