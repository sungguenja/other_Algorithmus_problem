N=int(input())
test_room = list(map(int,input().split()))
represent,viewer = map(int,input().split())
cnt = 0
for i in range(N):
    if test_room[i]<=represent:
        cnt+=1
    else:
        cnt+=1
        test_room[i]-=represent
        cnt += test_room[i]//viewer
        if test_room[i]%viewer:
            cnt+=1
print(cnt)