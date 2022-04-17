from itertools import combinations_with_replacement
def checkHowDifferentPoint(appeach,lion):
    lion_point_array = [0]*11
    for i in lion:
        lion_point_array[10-i] += 1
    appeach_point = 0
    lion_point = 0
    for i in range(11):
        if appeach[i] == 0 and lion_point_array[i] == 0:
            continue

        if appeach[i] >= lion_point_array[i]:
            appeach_point += 10 - i
        else:
            lion_point += 10 - i

    return lion_point > appeach_point,lion_point-appeach_point,lion_point,lion_point_array

def solution(n, info):
    answer = [0]*11
    win_point = 0
    now_point = 0

    lion_case = combinations_with_replacement(range(11),n)
    for lion in lion_case:
        is_win, tmp_win_point, tmp_lion_point, tmp_array = checkHowDifferentPoint(info,lion)
        if is_win:
            if win_point < tmp_win_point:
                win_point = tmp_win_point
                now_point = tmp_lion_point
                answer = tmp_array[:]
            elif win_point == tmp_win_point:
                for i in range(10,-1,-1):
                    if answer[i] < tmp_array[i]:
                        answer = tmp_array[:]
                        break
                    elif answer[i] > tmp_array[i]:
                        break
    
    if answer == [0]*11:
        return [-1]
    return answer