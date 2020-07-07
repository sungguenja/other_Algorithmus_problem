N = int(input())

synergy = [list(map(int,input().split())) for _ in range(N)] #시너지

root = []                           # 조합 경우의 수 뽑기
for i in range(1<<N):
    i_bin = list(bin(i)[2:])
    if i_bin.count('1') != N//2:
        continue
    z=[0]*(N//2)
    num=0
    for j in range(N):
        if i&(1<<j):
            z[num] = j
            num+=1
    root.append(z)

min_minus = N*10                # 최소값 저장용
hope = set(range(N))        # 상대팀 뽑기
while root != []:               # 모든 경우를 다 따진다
    Z=root.pop()
    X=list(hope-set(Z))
    start = 0
    link = 0
    for i in Z:
        for j in Z:
            start += synergy[i][j]
    for i in X:
        for j in X:
            link += synergy[i][j]
    if min_minus > abs(start-link):
        min_minus=abs(start-link)
    if min_minus == 0:
        break
print(min_minus)