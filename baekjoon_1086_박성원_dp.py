from sys import stdin
from math import gcd,factorial
input = stdin.readline

N = int(input().strip())

number_list = [-1]*N
length_list = [-1]*N
for i in range(N):
    now = input().strip()
    number_list[i] = int(now)
    length_list[i] = len(now)
K = int(input().strip())

dp = [[-1]*K for i in range(1<<N)]
remain_list = [[-1]*sum(length_list) for i in range(N)]

for i in range(N):
    for j in range(sum(length_list)):
        remain_list[i][j] = (number_list[i]*(10**j))%K

# 변수 설명
# now 현재 숫자의 길이, ex) 100 => 3
# visit 현재 방문 상황을 2진법으로 표현한다고 생각하면 됨
# rest 현재 나머지, if y = x + c => y%k = (x%k + c%k)%k
def solution(now,visit,rest):
    # 끝에 도달했을때 나머지의 유무, 나머지가 있다 갈 수 없는 곳으로 0 나머지가 없다 갈 수 있는 루트이므로 1
    if visit == (1<<N)-1:
        if rest == 0:
            return 1
        else:
            return 0
    
    # 도달한 경험이 있다 그럼 그 값을 리턴
    if dp[visit][rest] != -1:
        return dp[visit][rest]
    
    for i in range(N):
        if visit & (1<<i) == 0:
            dp[visit][rest] += solution(now+length_list[i],visit|(1<<i),(rest+remain_list[i][now])%K)
    
    dp[visit][rest] += 1
    return dp[visit][rest]

numerator = solution(0,0,0)
denominator = 1
if numerator != 0:
    F = factorial(N)
    now_gcd = gcd(F,numerator)
    numerator = numerator//now_gcd
    denominator = F//now_gcd

print('{0}/{1}'.format(numerator,denominator))