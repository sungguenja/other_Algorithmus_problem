from collections import deque

def solution(n, wires):
    answer = n * len(wires)
    visit = [None]*(n+1)
    routes = [[] for i in range(n+1)]
    for wire in wires:
        routes[wire[0]].append(wire[1])
        routes[wire[1]].append(wire[0])
    
    def bfs(cant_go_left,cant_go_right):
        Que = deque()
        left_cnt = -1
        right_cnt = -1
        left = 'left'
        right = 'right'
        visit[cant_go_left] = left
        visit[cant_go_right] = right
        Que.append((cant_go_left,left))
        Que.append((cant_go_right,right))
        while Que:
            now,where = Que.popleft()
            
            for goal in routes[now]:
                if (now == cant_go_left and goal == cant_go_right) or (now == cant_go_right and goal == cant_go_left):
                    continue
                if visit[goal] == None:
                    visit[goal] = where
                    Que.append((goal,where))
                elif visit[goal] != where:
                    return False
        
        return True
    
    for wire in wires:
        visit = [None]*(n+1)
        trigger = bfs(wire[0],wire[1])
        if trigger:
            none_cnt = 0
            left_cnt = 0
            right_cnt = 0
            for i in range(1,n+1):
                if visit[i] == None:
                    none_cnt += 1
                    break
                if visit[i] == 'left':
                    left_cnt += 1
                else:
                    right_cnt += 1
            if none_cnt < 1 and answer > abs(left_cnt-right_cnt):
                answer = abs(left_cnt-right_cnt)
    return answer