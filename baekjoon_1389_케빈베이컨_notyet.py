def bfs(start,end,visit):
    que = [[start,visit]]

    while que != []:
        z=que.pop()
        X,used = z[0],z[1]
        cnt=len(visit)
        while X < len(visit):
            if start == end and z>sum(used):
                cnt=sum(used)
                break
            if used[X] == 0 and friend[start][X] == 1:
                used[X] = 1
                que.append([X,used])
                used[X] = 0
                X+=1
            else:
                X+=1
    return cnt

N,M = map(int,input().split())

friend = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    fre1, fre2 = map(int,input().split())
    friend[fre1][fre2] = 1
    friend[fre2][fre1] = 1


for i in range(1,N+1):
    su = 0
    for j in range(1,N+1):
        if i==j:
            continue
        visit=[0]*N
        print(bfs(i,j,visit))
        