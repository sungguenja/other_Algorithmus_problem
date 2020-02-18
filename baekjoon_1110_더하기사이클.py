N=int(input())
a=N%10
b=N//10
c=a+b
d=c%10+a*10
cnt=1
while d!=N:
    a=d%10
    b=d//10
    c=a+b
    d=c%10+a*10
    cnt+=1
print(cnt)