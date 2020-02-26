first = list(input())
secon = list(input())

maximum_len = 0
for i in range(len(first)):
    now_len = 0
    ni = i
    nj = ni
    k = i
    while ni<len(first):
        while nj<len(secon):
            if secon[nj]==first[ni]:
                now_len+=1
                nj+=1
                k=nj
                break
            else:
                nj += 1
        ni += 1
        nj = k
    if maximum_len < now_len:
        maximum_len = now_len

print(maximum_len)