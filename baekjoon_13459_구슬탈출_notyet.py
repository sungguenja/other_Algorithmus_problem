d =[[0,1],[1,0],[0,-1],[-1,0]]

def game(n,ir,jr,ib,jb,cnt,dir):        # 게임판
    global counting
    if cnt==1:
        if counting>n:
            counting=n
    elif cnt>1:
        return
    elif n==10:
        return
    else:
        for k in range(len(d)):
            if dir==-1 or (k!=dir and k!=(dir+2)%4):
                p=[ir,jr,ib,jb]
                cnt, p = moving(p, k)
                if cnt == 0 and ir == p[0] and jr==p[1] and ib==p[2] and jb==p[3]:
                    continue
                else:
                    game(n+1,p[0],p[1],p[2],p[3],cnt,k)

def moving(p, go):         # 재귀 한도 뜰 각이어서 움직이는거 따로만들기
    nir, njr = p[0],p[1]
    nib, njb = p[2],p[3]
    cnt = 0
    while ball[nir+d[go][0]][njr+d[go][1]]!='#' and ball[nir+d[go][0]][njr+d[go][1]]!='O':
        nir+=d[go][0]
        njr+=d[go][1]
    if ball[nir+d[go][0]][njr+d[go][1]] == 'O':
        cnt+=1
    
    while ball[nib+d[go][0]][njb+d[go][1]]!='#' and ball[nib+d[go][0]][njb+d[go][1]]!='O':
        nib+=d[go][0]
        njb+=d[go][1]
    if ball[nib+d[go][0]][njb+d[go][1]] == 'O':
        cnt+=2

    if cnt>0:
        return cnt,p

    if nir==nib and njr==njb:           # 겹치는 경우
        if go==0:
            if p[1]<p[3]:               # 공들의 초기 위치로 상황 판단하기
                njr-=1
            else:
                njb-=1
            p=[nir,njr,nib,njb]
        elif go==1:
            if p[0]<p[2]:
                njb-=1
            else:
                njr-=1
        elif go==2:
            if p[1]<p[3]:
                njb+=1
            else:
                njr+=1
        elif go==3:
            if p[0]<p[2]:
                nib+=1
            else:
                nir+=1
        p=[nir,njr,nib,njb]
    else:
        p=[nir,njr,nib,njb]
    
    return cnt,p


N,M=map(int,input().split())
ball = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if ball[i][j] == 'R':
            R_point = [i,j]
            ball[i][j] = '.'
        if ball[i][j] == 'B':
            B_point = [i,j]
            ball[i][j] = '.'

counting = 12
game(0,R_point[0],R_point[1],B_point[0],B_point[1],0,-1)
if counting == 12:
    counting = -1
print(counting)