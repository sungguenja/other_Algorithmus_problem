A,B,V = map(int,input().split())

C=(V-B)//(A-B)
D=(V-B)%(A-B)

if D != 0:
    print(C+1)
else:
    print(C)