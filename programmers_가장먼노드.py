from collections import deque
def bfs(start,road,n):
    visit = [-1]*(n+1)
    Que = deque()
    Que.append((start,0))
    while Que:
        now, distance = Que.popleft()
        if visit[now] == -1:
            visit[now] = distance
            distance += 1
            for goal in road[now]:
                Que.append((goal,distance))
    return visit

def solution(n, edge):
    road = [[] for _ in range(n+1)]
    for left, right in edge:
        road[left].append(right)
        road[right].append(left)
    length_list = bfs(1,road,n)
    maximum_length = -1
    answer = 0
    for length in length_list:
        if maximum_length < length:
            answer = 1
            maximum_length = length
        elif maximum_length == length:
            answer += 1
    return answer