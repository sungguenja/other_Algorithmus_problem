N=int(input())              # 당근갯수

direct = []                 # 방향
distance = []               # 거리 체크용
for _ in range(6):
    di,dis = map(int, input().split())
    direct.append(di)
    distance.append(dis)

A = [4,2,3,1,3,1]                   # 방향체크용 
B = [1,4,2,3,2,3]                   # 나온 순서대로 ㄱ인지 ㄴ인지 모양판별가능
C = [1,4,2,4,2,3]
D = [1,4,1,4,2,3]
while direct != A and direct != B and direct != C and direct != D:
    direct[0],direct[1],direct[2],direct[3],direct[4],direct[5] = direct[1],direct[2],direct[3],direct[4],direct[5],direct[0]
    distance[0],distance[1],distance[2],distance[3],distance[4],distance[5] = distance[1],distance[2],distance[3],distance[4],distance[5],distance[0]
if direct == A or direct == B:
    print((distance[0]*distance[1]-distance[3]*distance[4])*N)
elif direct == C:
    print((distance[0]*distance[5]-distance[2]*distance[3])*N)
else:
    print((distance[4]*distance[5]-distance[1]*distance[2])*N)