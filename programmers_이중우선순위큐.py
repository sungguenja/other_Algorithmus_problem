# def solution(operations):
#     answer = []
#     for oper in operations:
#         if oper[0] == 'I':
#             answer.append(int(oper[2:]))
#         else:
#             if answer != []:
#                 if oper[2:] == '1':
#                     answer.pop(answer.index(max(answer)))
#                 else:
#                     answer.pop(answer.index(min(answer)))
#     if answer == []:
#         answer = [0,0]
#     else:
#         answer = [max(answer),min(answer)]
#     return answer
# 위는 index와 max, min이 들어가있어서 의외로 좀 느림
import heapq
def solution(operations):
    answer = []
    for oper in operations:
        if oper[0] == 'I':
            heapq.heappush(answer,int(oper[2:]))
        else:
            if answer != []:
                if oper[2:] == '1':
                    answer.pop(answer.index(max(answer)))
                else:
                    heapq.heappop(answer)
    if answer == []:
        answer = [0,0]
    else:
        answer = [max(answer),min(answer)]
    return answer
# 대충 heapq와 리스트 방식 섞은 것 이게 약간 더 빠름


print(solution(['I 16','D 1']))
print(solution(['I 7','I 5','I -5','D -1']))