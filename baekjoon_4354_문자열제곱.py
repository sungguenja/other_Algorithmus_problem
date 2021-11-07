while True:
    now_string = input()
    if now_string == '.':
        break
    start = 1
    base = now_string[0]
    while start < len(now_string):
        print(base,start)
        if now_string[start:start+len(base)] != base:
            tmp = start + len(base)
            base = now_string[:tmp]
            start = tmp
        else:
            start += len(base)
    print(len(now_string)//len(base),base)