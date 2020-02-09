N=int(input())

switch = [0]*(N+1)
switch[1:] = list(map(int, input().split()))

for _ in range(int(input())):
    gen, numb = map(int,input().split())
    if gen == 1:
        for i in range(1,N//numb + 1):
            switch[i*numb] = (switch[i*numb]+1)%2
    else:
        i = 1
        while switch[numb-i] == switch[numb+i]:
            i += 1
            if numb-i==1 or numb+i==N:
                break
        for j in range(numb-i,numb+i+1):
            switch[j] = (switch[j]+1)%2
    
for i in range(len(switch)//20+1):
    print(' '.join(map(str, switch[20*i+1:20*(i+1)+1])))