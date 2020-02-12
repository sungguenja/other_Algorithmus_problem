for _ in range(int(input())):
    H,W,N = map(int,input().split())
    X=N//H+1
    Y=N%H
    if Y!=0:
        print(Y*100+X)
    else:
        print(H*100+X-1)