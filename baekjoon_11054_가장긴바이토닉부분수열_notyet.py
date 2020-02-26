N=int(input())
num_list = list(map(int,input().split()))

max_len = 0
for i in range(1,N):
    num_rank_left = [0]*(i+1)
    num_rank_right = [0]*(N-i+1)
    z=0
    for j in range(i-1,-1,-1):
        if num_list[j]>num_list[i]:
            z+=1
            num_rank_left[j]=z
        else:
            num_rank_left[j]=z
    z=0
    num=0
    for j in range(i,N):
        if num_list[j]<num_list[i]:
            z+=1
            num_rank_right[num] = z
            num+=1
        else:
            num_rank_right[num] = z
            num+=1
    print(num_rank_left,num_rank_right)