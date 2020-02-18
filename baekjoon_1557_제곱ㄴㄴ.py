K=int(input())
K_list = list(range(1,K))
x=0
while len(K_list) < K:
    x+=1
    K_list.extend(list(range(x*K,(x+1)*K)))
    for i in range(2,len(K_list)):
        if i**2>K**2+1:
            break
        for z in range(1,K_list[-1]//(i**2)+1):
            try:
                K_list.remove(z*i**2)
            except ValueError:
                break
print(K_list[K])