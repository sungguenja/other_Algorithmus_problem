N=int(input())
numb_list = []
for _ in range(N):
    numb_list.append(int(input()))

make_list = []
num = 0
print_line = []
for i in range(1,N+1):
    make_list.append(i)
    print_line.append('+')
    while numb_list[num] == make_list[-1]:
        make_list.pop()
        print_line.append('-')
        num += 1
        if num >= len(numb_list) or len(make_list) == 0:
            break
if make_list != []:
    print('NO')
else:
    for k in print_line:
        print(k)