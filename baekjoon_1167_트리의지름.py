from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

route = [[] for i in range(N+1)]
for _ in range(N):
    arr = list(map(int,input().split()))
    start = arr[0]
    for i in range(1,len(arr)-2,2):
        goal,cost = arr[i],arr[i+1]
        route[start].append((goal,cost))

answer = -1
def dfs(start):
    global answer
    visit = [-1]*(N+1)
    Stack = deque()
    Stack.append(start)
    maximum_node = [0,0]
    visit[start] = 0
    while Stack:
        start = Stack.pop()
        
        for line in route[start]:
            goal,next_cost = line[0],line[1]+visit[start]
            if visit[goal] == -1:
                visit[goal] = next_cost
                Stack.append(goal)
                if maximum_node[0] < next_cost:
                    maximum_node = [next_cost,goal]
    
    return maximum_node

answer,other_start = dfs(1)
answer,other_start = dfs(other_start)

print(answer)