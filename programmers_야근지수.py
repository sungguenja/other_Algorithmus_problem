import heapq
def minus(x):
    return -1*x
def squre(x):
    return x**2
def solution(n, works):
    works = list(map(minus,works))
    heapq.heapify(works)
    for _ in range(n):
        now = heapq.heappop(works)
        if now>=0:
            break
        now += 1
        heapq.heappush(works,now)
    answer = sum(list(map(squre,works)))
    return answer

print(solution(4,[4,3,3]))
print(solution(1,[2,1,2]))
print(solution(3,[1,1]))