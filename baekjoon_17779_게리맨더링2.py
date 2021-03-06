N=int(input())
city = [list(map(int,input().split())) for i in range(N)]
answer = 100*((N+1)**2)
def solution(start_i,start_j,now_i,now_j,d_1=0,d_2=0,trigger=0):
    global answer
    if trigger==0:
        ni = now_i-1
        nj = now_j+1
        if 0<=ni<N and 0<=nj<N:
            solution(start_i,start_j,ni,nj,d_1+1,d_2,trigger)
        if d_1>=1:
            solution(start_i,start_j,now_i,now_j,d_1,d_2,trigger+1)
    elif trigger==1:
        ni = now_i+1
        nj = now_j+1
        di = start_i+d_2+1
        dj = start_j+d_2+1
        if 0<=ni<N and 0<=nj<N and 0<=di<N and 0<=dj<N:
            solution(start_i,start_j,ni,nj,d_1,d_2+1,trigger)
        if d_2>=1:
            solution(start_i,start_j,now_i,now_j,d_1,d_2,trigger+1)
    else:
        people = [0,0,0,0,0]
        for i in range(N):
            for j in range(N):
                if 0<=i<start_i and 0<=j<=start_j+d_1:
                    if i+j<start_i+start_j:
                        people[0] += city[i][j]
                    else:
                        people[4] += city[i][j]
                elif 0<=i<=start_i-d_1+d_2 and start_j+d_1<j<N:
                    if abs(i-j)>abs(start_j-start_i+2*d_1):
                        people[1] += city[i][j]
                    else:
                        people[4] += city[i][j]
                elif start_i<=i<N and 0<=j<start_j+d_2:
                    if abs(i-j)>abs(start_i-start_j):
                        people[2] += city[i][j]
                    else:
                        people[4] += city[i][j]
                elif start_i-d_1+d_2<i<N and start_j+d_2<=j<N:
                    if i+j > start_i+d_2+start_j+d_2:
                        people[3] += city[i][j]
                    else:
                        people[4] += city[i][j]
        if answer > abs(min(people)-max(people)):
            answer = abs(min(people)-max(people))
        return
for i in range(N):
    for j in range(N):
        solution(i,j,i,j)
print(answer)