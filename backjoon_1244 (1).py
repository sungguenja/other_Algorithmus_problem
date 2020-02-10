N=int(input())

switch = list(map(int, input().split()))

for _ in range(int(input())):
    gen, numb = map(int, input().split())
    if gen == 1:
        for i in range(numb-1,N,numb):
            switch[i] = (switch[i]+1)%2
    else:
        i=1
        while switch[numb-i-1] == switch[numb-1+i]:
            if numb-i<=0 or numb+i>=N:
                break
            i+=1
        for z in range(numb-i,numb+i-1):
            switch[z] = (switch[z]+1)%2
print(' '.join(map(str, switch)))