dragon = [[0]*110 for _ in range(110)]

direction = [[1,0],[0,-1],[-1,0],[0,1]]
for _ in range(int(input())):               # 인풋 받아준 만큼만 선이 생김
    x,y,d,g = map(int,input().split())
    dragon[y][x] += 1
    nx,ny=x+direction[d][0],y+direction[d][1]
    dragon[ny][nx] += 1   # 0세대는 미리 만들자
    now_d = [d]             # 전세대 저장용
    for i in range(1,g+1):
        now_g = []          # 현세대 늘어나는 양 저장
        for j in range(len(now_d)-1,-1,-1): # 거꾸로 읽는다
            nd=now_d[j]
            nx=nx+direction[(nd+1)%4][0]   # 방향을 오위왼아순으로 줘서 이러면 끝
            ny=ny+direction[(nd+1)%4][1]
            dragon[ny][nx] += 1
            now_g.append((nd+1)%4)
        else:
            for j in range(len(now_g)):
                now_d.append(now_g[j])      # 세대 저장을 한다

sq = 0
for i in range(101):
    for j in range(101):
        if dragon[i][j] >= 1 and dragon[i+1][j] >= 1 and dragon[i][j+1] >= 1 and dragon[i+1][j+1] >= 1: #자기위치와 오른쪽 오른쪽아래 아래에 있으면 사각형
            sq += 1
print(sq)