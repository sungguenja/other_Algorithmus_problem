N,M = map(int,input().split())
chicken = [0]*N
chicken_seller = []
house = []
for i in range(N):
    chicken[i] = list(map(int,input().split()))
    for j in range(N):
        if chicken[i][j] == 1:
            house.append([i,j])
        elif chicken[i][j] == 2:
            chicken_seller.append([i,j])

answer = (N**2)*len(chicken_seller)*len(house)

def chicken_distance(selected):
    global answer
    total_distance = 0
    for i in range(len(house)):
        now_distance = N**2
        for j in range(len(selected)):
            if now_distance>abs(selected[j][0]-house[i][0])+abs(selected[j][1]-house[i][1]):
                now_distance = abs(selected[j][0]-house[i][0]) + abs(selected[j][1]-house[i][1])
        total_distance += now_distance
        if total_distance>=answer:
            return False
    answer = total_distance
    return True

def solution(amount,idx=-1,cnt=0,select=[]):
    if amount == cnt:
        chicken_distance(select)
        return
    
    for i in range(idx+1,len(chicken_seller)):
        solution(amount,i,cnt+1,select+[chicken_seller[i]])

for i in range(1,M+1):
    solution(i)

print(answer)