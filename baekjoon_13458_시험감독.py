N=int(input())
test_room = list(map(int,input().split()))
B,C=map(int,input().split())
viewer = 0
for i in range(N):
    test_room[i] -= B
    viewer += 1
    if test_room[i] <= 0:
        continue
    else:
        if test_room[i]%C == 0:
            viewer += test_room[i]//C
        else:
            viewer += test_room[i]//C+1
print(viewer)