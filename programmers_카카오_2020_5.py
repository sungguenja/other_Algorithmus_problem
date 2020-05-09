def solution(n, path, order):
    answer = False
    road = [[0]*n for _ in range(n)]
    for i in path:
        road[i[0]][i[1]] = 1
        road[i[1]][i[0]] = 1
    que = [[0,[],set()]]
    while que != []:
        now = que.pop(0)
        where, root,visit = now[0],now[1],now[2]
        if len(visit) == n:
            answer = True
            break
        if len(root) == n**n:
            break
        for k in range(n):
            trigger = False
            if road[where][k] == 1:
                for t in order:
                    if t[1] in root and t[0] in root:
                        if root.index(t[1]) < root.index(t[0]):
                            trigger = True
                            break
            if not trigger:
                visit.add(k)
                que.append([k,root+[k],visit])
                visit.remove(k)
    return answer