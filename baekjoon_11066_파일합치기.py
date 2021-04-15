import heapq
def printAnswer(arr):
    answer = 0
    heapq.heapify(arr)
    while len(arr)>=2:
        now = 0
        now += heapq.heappop(arr)
        now += heapq.heappop(arr)
        answer += now
        heapq.heappush(arr,now)
    print(answer)

N = int(input())
for t in range(N):
    K = int(input())
    file_list = list(map(int,input().split()))
    printAnswer(file_list)