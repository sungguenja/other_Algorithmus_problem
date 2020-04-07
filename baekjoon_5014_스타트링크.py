F,S,G,U,D = map(int,input().split())
building = [None]*(F+1)
direction = [U,-D]
building[S] = 0
ans = 'use the stairs'
que = [S]
while que != []:
    now = que.pop(0)
    if now == G:
        ans=building[now]
        break
    for k in direction:
        now_k = now + k
        if 0<now_k<=F:
            if building[now_k] == None or building[now_k]>building[now]+1:
                building[now_k]=building[now]+1
                que.append(now_k)
print(ans)
print(building)