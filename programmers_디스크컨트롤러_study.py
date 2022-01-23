import heapq
def solution(jobs):
    answer = 0
    start = -1
    end,i = 0,0
    disk_heap = []
    while len(jobs) > i:
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(disk_heap,(job[1],job[0]))
        if len(disk_heap) > 0:
            now = heapq.heappop(disk_heap)
            start = end
            end += now[0]
            answer += end - now[1]
            i += 1
        else:
            end += 1
    return answer // len(jobs)