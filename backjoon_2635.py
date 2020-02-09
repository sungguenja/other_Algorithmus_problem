N=int(input())
numb_list = [N]
numb_len = 0
for i in range(N,-1,-1):
    before_numb = N
    next_num = i
    numb_list.append(i)
    while before_numb - next_num >= 0:
        t = before_numb
        before_numb = next_num
        next_num =  t - next_num
        numb_list.append(next_num)
    if numb_len < len(numb_list):
        numb_len = len(numb_list)
        save_numb = [0]*numb_len
        for i in range(numb_len):
            save_numb[i] = numb_list[i]
    numb_list = [N]
print(numb_len)
print(' '.join(map(str, save_numb)))