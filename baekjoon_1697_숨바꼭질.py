N,M = map(int,input().split())
line = [0]*100001
visit = [0]*100001

line[N] = 0
line[M] = 'B'

direct = [1,-1,2]

stack = [N]
trigger = 0
if N!=M:
    while stack != []:
        x = stack.pop(0)
        for k in range(len(direct)):
            if k == 2:
                if x*2 < 100001:
                    if line[2*x] == 0 and visit[2*x] == 0:
                        line[2*x] = line[x] + 1
                        stack.append(2*x)
                        visit[2*x] = 1
                    elif line[2*x] == 'B':
                        line[2*x] = ['B',line[x]+1]
                        trigger = 1
                        break
            else:
                if 0<= x+direct[k] < 100001:
                    if line[x+direct[k]] == 0 and visit[x+direct[k]] == 0:
                        line[x+direct[k]] = line[x] + 1
                        stack.append(x+direct[k])
                        visit[x+direct[k]] = 1
                    elif line[x+direct[k]] == 'B':
                        line[x+direct[k]] = ['B', line[x]+1]
                        trigger = 1
                        break
        if trigger == 1:
            break
    print(line[M][1])
else:
    print(0)