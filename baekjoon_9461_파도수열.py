pado = [0,1,1,1,2,2,3,4,5,7,9]

for t in range(int(input())):
    N=int(input())
    while len(pado) <= N+1:
        pado.append(pado[N-2]+pado[N-3])
    print(pado[N])