# # min_time = 500000
# # def solution(jobs,end_time=0,visit=[],answer=0):
# #     global min_time
# #     if len(visit) == len(jobs):
# #         if answer//3 < min_time:
# #             min_time = answer//3
# #         return
# #     else:
# #         for i in range(len(jobs)):
# #             if i not in visit:
# #                 if end_time<=jobs[i][0]:
# #                     solution(jobs,end_time+jobs[i][0]+jobs[i][1],visit+[i],answer+end_time+jobs[i][0]+jobs[i][1])
# #                 else:
# #                     solution(jobs,end_time+jobs[i][1],visit+[i],answer+end_time+jobs[i][1]-jobs[i][0])
# #     return min_time
# def solution(jobs):
#     jobs.sort()
#     visit = [0]*len(jobs)
#     answer = jobs[0][1]
#     end_time = jobs[0][1]+jobs[0][0]
#     visit[0] = 1
#     while visit != [1]*len(jobs):
#         now_delay = 0
#         now_end = end_time
#         for i in range(len(jobs)):
#             if visit[i] == 0:
#                 if jobs[i][0] < end_time:
#                     if now_delay == 0 or now_delay>end_time
# print(solution([[0, 3], [1, 9], [2, 6]]))
# import heapq
# heap = []
# heapq.heappush(heap,3)
# print(heap)
# heapq.heappush(heap,2)
# print(heap)
# heapq.heappush(heap,4)
# print(heap)
# heapq.heappush(heap,1)
# print(heap)
# def solution(jobs):
#     import heapq

#     # 1. jobs 정렬
#     jobs.sort()
#     answer = 0
#     n = 0
#     # 2. 최초 시간 설정
#     time = jobs[0][0]
#     # 3. 우선순위 큐 생성
#     pq = []
    
#     # 4. job이 빌 떄까지 다음을 반복합니다.
#     while jobs:
#         # 1. jobs의 첫 원소를 꺼내옵니다.
#         (request, expend) = jobs.pop(0)
#         # 2. n에 1을 더해줍니다.
#         n += 1
#         # 3. time에 소요 시간 expend를 더해줍니다.
#         time += expend
#         # 4. answer에 현재 시간 time에서 요청 시간 request를 뺸 값을 더해줍니다.
#         answer += (time - request)
#         print(answer,n,time,request,expend,jobs,pq)
        
#         # 5. jobs가 비지 않고, jobs[0][0]일 떄 다음을 반복합니다.
#         while jobs and jobs[0][0] < time:
#             # 1. jobs의 첫 원소를 꺼내옵니다.
#             (request, expend) = jobs.pop(0)
#             # 2. 해당 원소를 expend 기준으로 pq에다 저장합니다.
#             heapq.heappush(pq, (-expend, request))
#         print(answer,n,time,request,expend,jobs,pq)

#         # 6. pq가 빌 떄까지 다음을 반복합니다.
#         while pq:
#             # 1. pq에서 원소를 꺼냅니다.
#             (expend, request) = heapq.heappop(pq)
#             # 2. jobs에 첫 원소로 저장합니다.
#             jobs.insert(0, [request, -expend])
#         print(answer,n,time,request,expend,jobs,pq)

#     # 5. answer에 n을 나눠준 몫을 저장하고 반환합니다.
#     answer //= n
#     return answer
# def solution(jobs):
#     answer = 0
#     jobs.sort(key= lambda x:x[1])
#     end = 0
#     for i in jobs:
#         end = end+i[1]
#         answer += end-i[0]
#     return answer//len(jobs)
def solution(jobs):
    num_jobs = len(jobs)
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    print(jobs)
    start, time = jobs.pop(0)
    end = time+start
    answer += time
    while jobs:
        nxt_idx = 0
        for idx in range(1, len(jobs)):
            if jobs[idx][0] > end:
                break
            else:
                if jobs[idx][1] < jobs[nxt_idx][1]:
                    nxt_idx = idx
        nxt = jobs.pop(nxt_idx)
        if nxt[0] <= end:
            answer += nxt[1] + (end - nxt[0])
            end += nxt[1]
        else:
            answer += nxt[1]
            end = sum(nxt)

    return answer // num_jobs

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 3], [0, 9], [0, 6]]))