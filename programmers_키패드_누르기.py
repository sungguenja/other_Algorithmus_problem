def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    center = [2,5,8,0]
    lh = [3,0]
    rh = [3,2]
    for i in range(len(numbers)):
        if numbers[i] in left:
            answer += 'L'
            lh = [left.index(numbers[i]),0]
        elif numbers[i] in right:
            answer += 'R'
            rh = [right.index(numbers[i]),2]
        else:
            cc = center.index(numbers[i])
            ld = abs(lh[0]-cc)+abs(lh[1]-1)
            rd = abs(rh[0]-cc)+abs(rh[1]-1)
            if ld > rd:
                answer += 'R'
                rh = [cc,1]
            elif ld < rd:
                answer += 'L'
                lh = [cc,1]
            else:
                if hand == 'right':
                    answer += 'R'
                    rh = [cc,1]
                else:
                    answer += 'L'
                    lh = [cc,1]
    return answer