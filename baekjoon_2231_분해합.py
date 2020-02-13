N=int(input())
M=N//2
C=M
i=1
while True:
    X = list(str(C))    
    for k in X:
        C += int(k)
    if C==N:
        break
    else:
        C=M+i
        C_save = C
        i+=1
