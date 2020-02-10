N=int(input())
numb_list = list(map(int, input().split()))
numb_list.append(0)
numb_len = 1
save_len = 0
for i in range(N):
    if numb_list[i] <= numb_list[i+1]:
        numb_len += 1
    else:
        if save_len<numb_len:
            save_len=numb_len
        numb_len = 1
print(save_len)