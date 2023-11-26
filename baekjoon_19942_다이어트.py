from sys import stdin
from itertools import combinations

input = stdin.readline

N = int(input())
answer = 999999
answerList = []
mp,mf,ms,mv = map(int,input().split())
foodList = [list(map(int,input().split())) for _ in range(N)]
choiceList = [i for i in range(N)]
for food in foodList:
    answer += food[4]
bornAnswer = answer

for i in range(1,N+1):
    combi = list(combinations(choiceList,i))
    for choice in combi:
        protean = 0
        fat = 0
        carbon = 0
        vitamin = 0
        cost = 0
        for i in choice:
            protean += foodList[i][0]
            fat += foodList[i][1]
            carbon += foodList[i][2]
            vitamin += foodList[i][3]
            cost += foodList[i][4]
        if protean >= mp and fat >= mf and carbon >= ms and vitamin >= mv:
            if cost < answer:
                answer = cost
                answerList = [str(x + 1) for x in choice]
            elif cost == answer:
                beforeAnswer = ''.join(answerList)
                nowAnswer = ' '.join(str(x + 1) for x in choice)
                if nowAnswer < beforeAnswer:
                    answerList = [str(x + 1) for x in choice]

if bornAnswer == answer:
    print(-1)
else:
    print(answer)
    print(' '.join(answerList))