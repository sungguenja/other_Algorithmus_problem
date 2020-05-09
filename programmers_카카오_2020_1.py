def solution(numbers, hand):
    answer = ''
    num_pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left = [1,4,7,'*']
    right = [3,6,9,'#']
    center = [2,5,8,0]
    L = [3,0]
    R = [3,2]
    for i in range(len(numbers)):
        if numbers[i] in left:
            for k in range(4):
                if num_pad[k][0] == numbers[i]:
                    L = [k,0]
                    answer += 'L'
                    break
        elif numbers[i] in right:
            for k in range(4):
                if num_pad[k][2] == numbers[i]:
                    R = [k,2]
                    answer += 'R'
                    break
        elif numbers[i] in center:
            for k in range(4):
                if num_pad[k][1] == numbers[i]:
                    if abs(k-L[0]) + abs(1-L[1]) > abs(k-R[0]) + abs(1-R[1]):
                        R = [k,1]
                        answer += 'R'
                    elif abs(k-L[0]) + abs(1-L[1]) < abs(k-R[0]) + abs(1-R[1]):
                        L = [k,1]
                        answer += 'L'
                    elif abs(k-L[0]) + abs(1-L[1]) == abs(k-R[0]) + abs(1-R[1]):
                        if hand == 'right':
                            R = [k,1]
                            answer += 'R'
                        elif hand == 'left':
                            L = [k,1]
                            answer += 'L'
                    break
    return answer

print(solution([1,1,1,1],'left'))