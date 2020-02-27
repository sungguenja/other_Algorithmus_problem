N=int(input())
num_list = [0]
num_list.extend(list(map(int,input().split())))

max_len = -1
for j in range(1,N+1):
    num_rank_left = [0]             # 왼쪽 오른쪽 나누기 위한 리스트
    num_list_left = [0]
    num_rank_right = [0]
    num_list_right = [1001]
    for i in range(j):            # 왼쪽은 중가하는 걸로
        if num_list_left[-1]<num_list[i]:
            num_rank_left.append(num_rank_left[-1]+1)
            num_list_left.append(num_list[i])
        else:
            for k in range(len(num_list_left)-1):
                if num_list_left[k] < num_list[i] < num_list_left[k+1]:
                    num_list_left[k+1] = num_list[i]
    
    for i in range(j,N+1):    #오른쪽은 감소하거나 거꾸로 증가하거나
        if num_list_right[-1]>num_list[i]:
            num_rank_right.append(num_rank_right[-1]+1)
            num_list_right.append(num_list[i])
        else:
            for k in range(len(num_rank_right)-1):
                if num_list_right[k] > num_list[i] > num_list_right[k+1]:
                    num_list_right[k+1] = num_list[i]
                    break

    if max_len<max(num_rank_left)+max(num_rank_right):  # 최대길이
        if num_list_left[-1]==num_list_right[1]:
            max_len=max(num_rank_left)+max(num_rank_right)-1
        else:
            max_len=max(num_rank_left)+max(num_rank_right)

print(max_len)