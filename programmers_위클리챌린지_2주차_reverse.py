def getAvg(my_scores,score_mine_to_me,N):
    same_trigger = 0
    middle_trigger = [False,False]
    total = 0
    for i in range(N):
        total += my_scores[i]
        if score_mine_to_me == my_scores[i]:
            same_trigger += 1
        elif score_mine_to_me < my_scores[i]:
            middle_trigger[0] = True
        elif score_mine_to_me > my_scores[i]:
            middle_trigger[1] = True
    if not middle_trigger[0] or not middle_trigger[1]:
        if same_trigger <= 1:
            total -= score_mine_to_me
            N -= 1
            
    return total / N

def getRank(my_scores,score_mine_to_me,N):
    score = getAvg(my_scores,score_mine_to_me,N)
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def reverseMatrix(matrix):
    result = [[0]*len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    return result

def solution(scores):
    answer = ''
    N = len(scores)
    reversed_matrix = reverseMatrix(scores)
    for i in range(N):
        answer += getRank(reversed_matrix[i],scores[i][i],N)
    return answer