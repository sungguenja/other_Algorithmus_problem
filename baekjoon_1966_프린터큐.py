for t in range(int(input())):
    N,M=map(int,input().split())
    que = list(map(int,input().split()))
    num=0
    for idx,value in enumerate(que):
        que[idx] = [idx,value]
    while True:
        for i in range(1,len(que)):
            if que[0][1]<que[i][1]:
                X=que.pop(0)
                que.append(X)
                break
        else:
            num+=1
            X=que.pop(0)
            if X[0]==M:
                break
    print(num)
