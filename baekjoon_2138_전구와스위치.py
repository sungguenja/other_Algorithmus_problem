N=int(input())
start = list(input())
save_start = start[:]
last = list(input())
answer = (N+1)**2
cnt = 0
for i in range(1,N):
    bi,ni,ai = i-1,i,i+1
    if start[bi] != last[bi]:
        cnt += 1
        if start[bi] == '1':
            start[bi] = '0'
        else:
            start[bi] = '1'
        if start[ni] == '1':
            start[ni] = '0'
        else:
            start[ni] = '1'
        if ai<N:
            if start[ai] == '1':
                start[ai] = '0'
            else:
                start[ai] = '1'
if start == last and cnt<answer:
    answer = cnt
cnt = 1
start = save_start[:]
if start[0] == '1':
    start[0] = '0'
else:
    start[0] = '1'
if start[1] == '1':
    start[1] = '0'
else:
    start[1] = '1'
for i in range(1,N):
    bi,ni,ai = i-1,i,i+1
    if start[bi] != last[bi]:
        cnt += 1
        if start[bi] == '1':
            start[bi] = '0'
        else:
            start[bi] = '1'
        if start[ni] == '1':
            start[ni] = '0'
        else:
            start[ni] = '1'
        if ai<N:
            if start[ai] == '1':
                start[ai] = '0'
            else:
                start[ai] = '1'
if start == last and cnt<answer:
    answer = cnt
if answer == (N+1)**2:
    answer = -1
print(answer)