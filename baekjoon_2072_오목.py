omok = [[3]*20 for _ in range(20)]
direct = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

for i in range(int(input())):
    N,M=map(int,input().split())
    N-=1
    M-=1
    omok[N][M] = i%2
    counting = 0
    t=0
    for j in range(len(direct)):
        if N+direct[j][0] < 0 or N+direct[j][0] >= 19 or M+direct[j][1] < 0 or M+direct[j][1] >=19:
            continue
        else:
            if omok[N+direct[j][0]][M+direct[j][1]] == omok[N][M]:
                counting = 0
                X,Y = N, M
                while omok[X][Y] == omok[N][M] and 19>X>=0 and 19>Y>=0:
                    counting += 1
                    X,Y = X+direct[j][0],Y+direct[j][1]
                X,Y = N+direct[(j+4)%8][0], M+direct[(j+4)%8][1]
                while omok[X][Y] == omok[N][M] and 19>X>=0 and 19>Y>=0:
                    counting += 1
                    X,Y = X+direct[(j+4)%8][0], Y+direct[(j+4)%8][1]
        if counting == 5:
            t=1
            break
    if t==1:
        print(i+1)
        break
else:
    print(-1)
