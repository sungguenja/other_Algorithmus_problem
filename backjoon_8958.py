for t in range(int(input())):
    omr = list(input())
    score = 0
    num = 0
    for i in range(len(omr)):
        if omr[i] == 'O':
            num += 1
            score += num
        else:
            num = 0
    print(score)