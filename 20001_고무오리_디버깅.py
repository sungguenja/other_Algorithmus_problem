n=0
start = input()
while True:
    command = str(input())
    if command == '문제':
        n += 1
    elif command == '고무오리':
        if n<=0:
            n+=2
        else:
            n-=1
    else:
        break
if n == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')