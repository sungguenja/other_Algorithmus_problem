horizon, vertical = map(int,input().split())    # my town's area

store = []                      # store position
for _ in range(int(input())):
    x = []
    x = list(map(int, input().split()))
    store.append(x)

police = list(map(int, input().split()))

distance = [0,0,0]

for i in range(3):
    if police[0] == 1:
        if store[i][0] == 1:
            distance[i] = abs(police[1]-store[i][1])
        elif store[i][0] == 2:
            distance[i] = 
        elif store[i][0] == 3:
            distance[i] = police[1] + N - store[i][1]
        else:
            distance