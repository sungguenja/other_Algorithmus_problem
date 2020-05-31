# answer = 0
# def find(n,case,now=0,start=0):
#     global answer
#     if n<now:
#         return
#     if n==now:
#         answer += 1
#         answer = answer%1000000007
#         return
#     for i in range(start,len(case)):
#         if now+case[i]<=n:
#             find(n,case,now+case[i],i)

# def solution(n, money):
#     global answer
#     find(n,money)
#     return answer
def solution(n, money):
    answer = [[0]*(n+1) for i in range(len(money))]
    answer[0][0] = 1
    for i in range(money[0],n+1,money[0]):
        answer[0][i] = 1
    for y in range(1,len(money)):
        for x in range(n+1):
            if x>=money[y]:
                answer[y][x] = (answer[y-1][x] + answer[y][x-money[y]])%1000000007
            else:
                answer[y][x] = answer[y-1][x]
    return answer[-1][-1]