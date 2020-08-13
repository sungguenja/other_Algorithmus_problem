def queing(x):
    return [x,0]
n,L,w = map(int,input().split())
Que = list(map(queing,(map(int,input().split()))))
cnt = 0
bridge = []
Save_que_len = len(Que)
after = []
while len(after) != Save_que_len:
    weight = 0
    can_go = 0
    for i in range(len(bridge)):
        weight += bridge[i][0]
        bridge[i][1] += 1
        if bridge[i][1]>=L:
            can_go += 1
            weight -= bridge[i][0]
    for i in range(can_go):
        after.append(bridge.pop(0))
    if len(after) == Save_que_len:
        cnt+=1
        break
    if len(Que) != 0:
        if weight + Que[0][0] <= w:
            bridge.append(Que.pop(0))
    cnt+=1
print(cnt)