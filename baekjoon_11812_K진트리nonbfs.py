import sys
input = sys.stdin.readline
def findDistance(start,goal,K):
    if K == 1:
        return abs(start-goal)
        
    start_level,goal_level = findLevel(start,goal,K)
    
    answer,start_level,goal_level,start,goal = makeSameLevelAndFindHowManyCountForMakingSameLevel(start_level,start,goal_level,goal,K)

    while start != goal:
        start = (start + K - 2) // K
        goal = (goal + K - 2) // K
        answer += 2
    
    return answer

def findLevel(start,goal,K):
    start_level = None
    goal_level = None
    left_limit = 1
    right_limit = 1
    cnt = 1
    while start_level == None or goal_level == None:
        if left_limit <= start <= right_limit:
            start_level = cnt
        if left_limit <= goal <= right_limit:
            goal_level = cnt
        
        left_limit = left_limit*K-(K-2)
        right_limit = right_limit*K+1
        cnt += 1

    return start_level,goal_level

def makeSameLevelAndFindHowManyCountForMakingSameLevel(start_level,start,goal_level,goal,K):
    cnt = 0
    while start_level != goal_level:
        if start_level > goal_level:
            start = (start + K - 2) // K
            start_level -= 1
        else:
            goal = (goal + K - 2) // K
            goal_level -= 1
        cnt += 1
    
    return cnt,start_level,goal_level,start,goal

N,K,Q = map(int,input().split())
for i in range(Q):
    start,goal = map(int,input().split())
    print(findDistance(start,goal,K))