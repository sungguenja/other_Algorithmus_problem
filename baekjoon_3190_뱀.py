direction = [[0,1],[1,0],[0,-1],[-1,0]]
def dummy(N,c_case):
    r,c,d = 1,1,0
    snake = [[r,c]]
    game_map[r][c] = 1
    t=0
    cnt=0
    while True:
        t+=1
        r+=direction[d][0]
        c+=direction[d][1]
        if 1<=r<=N and 1<=c<=N:
            if game_map[r][c] == 1:
                break
            else:
                if game_map[r][c] != 'A':
                    Z=snake.pop(0)
                    rr,cc=Z[0],Z[1]
                    game_map[rr][cc]=0
                snake.append([r,c])
                game_map[r][c] = 1
                
                if cnt<c_case and t==int(command[cnt][0]):
                    if command[cnt][1] == 'D':
                        d += 1
                        if d==4:
                            d=0
                        cnt+=1
                    elif command[cnt][1] == 'L':
                        d -= 1
                        if d==-1:
                            d=3
                        cnt+=1    
        else:
            break
    
    return t

N=int(input())
game_map = [[0]*(N+1) for _ in range(N+1)]
a = int(input())
for _ in range(a):
    apple_y,apple_x = map(int,input().split())
    game_map[apple_y][apple_x] = 'A'
c_case = int(input())
command = []
for _ in range(c_case):
    command.append(list(input().split()))
print(dummy(N,c_case))
