dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 11
def solution(cnt,ired,jred,iblue,jblue,case,direction):
    global answer
    if cnt>=answer:     # 지금 답보다 길면 더 돌지 않는다
        return

    if case>1:          # 파란공이 들어갔거나 같이 들어감
        return

    if case == 1:       # 빨간공만 들어감
        if cnt<answer:
            answer=cnt
        return
    
    for i in range(4):  # 아직 안들어감
        if direction==5 or (i != direction%4 and i != (direction+2)%4):
            ball = [ired,jred,iblue,jblue]
            case, moved_ball = moving(ball,i)
            # 공 움직이는 로직을 여기에 짜면 복잡해질 것 같아서
            if case == 0 and ired == moved_ball[0] and jred == moved_ball[1] and iblue == moved_ball[2] and jblue == moved_ball[3]:
                continue
            # 변화가 없는 경우
            else:
                solution(cnt+1,moved_ball[0],moved_ball[1],moved_ball[2],moved_ball[3],case,i)

def moving(location,way):
    nir,njr = location[0],location[1]
    nib,njb = location[2],location[3]
    now_case = 0
    
    while maze[nir+dy[way]][njr+dx[way]] != '#' and maze[nir+dy[way]][njr+dx[way]] != 'O':
        nir += dy[way]
        njr += dx[way]
    if maze[nir+dy[way]][njr+dx[way]] == 'O':
        now_case += 1   # 숫자 크기로 어떤 공이 들어갔는지 다르게 만들어줌

    while maze[nib+dy[way]][njb+dx[way]] != '#' and maze[nib+dy[way]][njb+dx[way]] != 'O':
        nib += dy[way]
        njb += dx[way]
    if maze[nib+dy[way]][njb+dx[way]] == 'O':
        now_case += 2
    
    if now_case>0:  # 공이 아무거나 들어감
        return now_case, [nir,njr,nib,njb]
    else:
        if nir==nib and njr==njb:   # 들어가지 않고 겹침
            if way==0:
                if location[1] > location[3]:
                    njb-=1
                else:
                    njr-=1
            elif way==1:
                if location[0] > location[2]:
                    nib-=1
                else:
                    nir-=1
            elif way==2:
                if location[1] < location[3]:
                    njb+=1
                else:
                    njr+=1
            elif way==3:
                if location[0] < location[2]:
                    nib+=1
                else:
                    nir+=1
        return now_case,[nir,njr,nib,njb]

N,M=map(int,input().split())
maze = [0]*N
cnt = 0
for i in range(N):
    maze[i] = list(input())
    if i!=0 and i!=N-1 and cnt!=3:
        for j in range(1,M-1):
            if maze[i][j] == 'B':
                blue = [i,j]
                cnt+=1
            if maze[i][j] == 'R':
                red = [i,j]
                cnt+=1
            if maze[i][j] == 'O':
                hole = [i,j]
                cnt+=1
solution(0,red[0],red[1],blue[0],blue[1],0,5)
if answer == 11:
    answer = -1
print(answer)