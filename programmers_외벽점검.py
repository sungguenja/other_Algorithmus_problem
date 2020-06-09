from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist)+1
    people_order = list(permutations(dist,len(dist)))
    for i in range(len(weak)):
        for j in people_order:
            fr_idx = 0
            start_point = weak[i]
            end_point = start_point + j[fr_idx]
            for k in range(i,i+len(weak)):
                if start_point<= weak[k%len(weak)] <= end_point or start_point<=weak[k%len(weak)]+n<=end_point:
                    continue
                else:
                    fr_idx+=1
                    if fr_idx>=len(dist) or fr_idx>=answer:
                        break
                    start_point = weak[k%len(weak)]
                    end_point = start_point + j[fr_idx]
            if fr_idx+1<answer:
                answer = fr_idx+1
    if answer > len(dist):
        answer = -1
    return answer

# from itertools import permutations
# def solution(n, weak, dist):
#     answer = len(dist)+1
#     for i in range(len(weak)):
#         people_order = permutations(dist,len(dist))
#         for j in people_order:
#             visit = [False]*len(weak)
#             idx = i
#             fr_idx = 0
#             while False in visit:
#                 if answer == 1:
#                     break
#                 if fr_idx>=len(j) or fr_idx>=answer:
#                     break
#                 start_point = weak[idx]
#                 end_point = start_point + j[fr_idx]
#                 for k in range(len(weak)):
#                     if visit[k]:
#                         continue
#                     if start_point<= weak[k] <= end_point or start_point<= weak[k]+n<= end_point:
#                         visit[k] = True
#                         idx += 1
#                         if idx>=len(weak):
#                             idx=idx%len(weak)
#                 if False in visit:
#                     fr_idx += 1
#                 else:
#                     if answer>fr_idx+1:
#                         answer = fr_idx+1
#                     break
#             if answer == 1:
#                 break
#         if answer == 1:
#             break
#     if answer == len(dist)+1:
#         answer = -1
#     return answer