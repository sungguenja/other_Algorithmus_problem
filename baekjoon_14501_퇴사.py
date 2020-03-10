N=int(input())
schedule=[[0]*(N+1) for _ in range(N)]
for i in range(N):
    dead,money=map(int,input().split())
    if i+dead<=N:
        for j in range(i,i+dead):
            schedule[i][j] = money
case = [[0]*N for _ in range(N)]
for i in range(N):
    if i == 0:                      # 시작점
        for j in range(N):
            case[i][j] = schedule[i][i]
    else:
        A = schedule[i][i]          # 이번 봉급은 얼마인가
        if schedule[i][i] == 0:     # 일을 할 수 없는 기간일 경우
            ni=i-1
            while ni>=0:
                nj=i
                while schedule[ni][nj] != 0 and nj>=0:
                    nj-=1
                if A<schedule[ni][nj]:
                    A=schedule[ni][nj]
                ni-=1
            for j in range(i,N):
                case[i][j] = max(A,case[i-1][j])
        else:           # 일해라 노예야 취업을 못해서 노예도 못됨 :biblethump:
            ni=i-1
            while ni>=0:    # 이 전의 받은 봉급 확인
                nj=i
                if schedule[ni][nj] == 0:   # 이 때의 일은 수령가능?
                    while schedule[ni][nj] == 0 and nj>=0:
                        nj-=1
                    if A<schedule[ni][nj]+schedule[i][i]:
                        A=schedule[ni][nj]+schedule[i][i]
                ni-=1
            nj = i
            while  0<=nj<N and schedule[i][nj] != 0:
                schedule[i][nj] = A
                nj+=1
            for j in range(i,N):
                case[i][j] = max(A,case[i-1][j])
print(case[-1][-1])