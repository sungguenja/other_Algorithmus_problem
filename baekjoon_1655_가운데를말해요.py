import heapq
max_heap = []
min_heap = []
for i in range(int(input())):
    if i == 0:
        heapq.heappush(max_heap,-int(input()))
        print(-max_heap[0])
        continue
    N = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,-N)
    else:
        heapq.heappush(min_heap,N)
    
    if -1*(max_heap[0])>min_heap[0]:
        temp_min = heapq.heappop(min_heap)
        temp_max = heapq.heappop(max_heap)
        heapq.heappush(min_heap,-1*(temp_max))
        heapq.heappush(max_heap,-temp_min)
    print(-max_heap[0])