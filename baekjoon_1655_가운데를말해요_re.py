import heapq
import sys
input = sys.stdin.readline
N = int(input())
max_heap = []
min_heap = []
heapq.heapify(max_heap)
heapq.heapify(min_heap)
for i in range(N):
    now = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-now)
    else:
        heapq.heappush(min_heap,now)
    if min_heap and min_heap[0] < -max_heap[0]:
        temp_max = heapq.heappop(max_heap)
        temp_min = heapq.heappop(min_heap)
        heapq.heappush(max_heap,-temp_min)
        heapq.heappush(min_heap,-temp_max)
    print(-max_heap[0])