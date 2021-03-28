from collections import deque
di = [0,1,0,-1]
dj = [1,0,-1,0]
N,M,fuel = map(int,input().split())
park = [list(map(int,input().split())) for i in range(N)]
taxi_i,taxi_j = map(int,input().split())
taxi_i -= 1
taxi_j -= 1
customers = [list(map(int,input().split())) for i in range(M)]

def findCustomer(taxi_i,taxi_j,member):
    Que = deque()
    Que.append((taxi_i,taxi_j,0))
    minimum_fuel = (N+1)**2
    goal_i = (N+1)**2
    goal_j = (N+1)**2
    goal = -1
    visit = [[False]*N for i in range(N)]
    while Que:
        i,j,count = Que.popleft()
        
        if count > minimum_fuel:
            continue
        
        if [i,j] in member:
            if count < minimum_fuel:
                minimum_fuel = count
                goal_i = i
                goal_j = j
                goal = member.index([i,j])
                continue
            elif count == minimum_fuel:
                if i < goal_i:
                    goal_i = i
                    goal_j = j
                    goal = member.index([i,j])
                    continue
                elif goal_i == i:
                    if j < goal_j:
                        goal_j = j
                        goal = member.index([i,j])
                        continue
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == False and park[ni][nj] == 0:
                visit[ni][nj] = True
                Que.append((ni,nj,count+1))
    
    return goal,minimum_fuel

def goGoal(taxi_i,taxi_j,goal):
    Que = deque()
    Que.append((taxi_i,taxi_j,0))
    minimum_fuel = (N+1)**2
    goal_point = -1
    visit = [[False]*N for i in range(N)]
    while Que:
        i,j,count = Que.popleft()
        
        if count >= minimum_fuel:
            continue

        if [i,j] == goal:
            goal_point = goal
            minimum_fuel = count
            break
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == False and park[ni][nj] == 0:
                visit[ni][nj] = True
                Que.append((ni,nj,count+1))
    
    return goal_point,minimum_fuel

while customers and fuel > 0:
    user,used_fuel = findCustomer(taxi_i,taxi_j,[[cust[0]-1,cust[1]-1] for cust in customers])
    
    if user == -1:
        fuel = -1
        break
    
    target = user
    user,used_fuel = goGoal(taxi_i,taxi_j,[customers[target][0]-1,customers[target][1]-1])
    if user == -1:
        fuel = -1
        break
    
    fuel -= used_fuel
    taxi_i,taxi_j = customers[target][0]-1,customers[target][1]-1
    
    user,used_fuel = goGoal(taxi_i,taxi_j,[customers[target][2]-1,customers[target][3]-1])
    if user == -1 or used_fuel > fuel:
        fuel = -1
        break

    fuel -= used_fuel
    fuel += used_fuel*2
    taxi_i,taxi_j = customers[target][2]-1,customers[target][3]-1
    customers.pop(target)

print(fuel)