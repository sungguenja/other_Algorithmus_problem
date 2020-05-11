def solution(n, edge):
    answer = 0
    ans = [0]*n
    road = [[] for _ in range(n)]
    for i,j in edge:
        road[i-1].append(j-1)
        road[j-1].append(i-1)
    start = 0
    que = [0]*n
    que[0] = [start,0]
    visit = [0]*n
    visit[start] = 1
    r=-1
    l=0
    while r<l:
        r+=1
        now = que[r]
        ready,distance = now[0],now[1]
        ans[ready] = distance
        for k in road[ready]:
            if visit[k]==0:
                l+=1
                que[l] = [k,distance+1]
                visit[k] = 1
    answer = ans.count(max(ans))
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))