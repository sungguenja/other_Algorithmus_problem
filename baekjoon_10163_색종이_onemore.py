color_paper = [[0]*101 for _ in range(101)]

N=int(input())
for x in range(1,N+1):
    start_x, start_y, horizon, vertical = map(int, input().split())
    for i in range(start_y,start_y+vertical):
        for j in range(start_x,start_x+horizon):
            color_paper[i][j] = x

for x in range(1,N+1):
    counting = 0
    for i in range(101):
        for j in range(101):
            if color_paper[i][j] == x:
                counting += 1
    print(counting)