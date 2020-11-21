def solution(gems):
    answer = []
    case = len(set(gems))
    start = 0
    end = 0
    gem_situation = {gems[0]:1}
    while start<len(gems):
        if len(gem_situation) == case:
            if (answer == []) or (end-start < answer[1]-answer[0]):
                answer = [start+1,end+1]
            if gem_situation[gems[start]] == 1:
                del gem_situation[gems[start]]
            else:
                gem_situation[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if gem_situation.get(gems[end]) == None:
                gem_situation[gems[end]] = 1
            else:
                gem_situation[gems[end]] += 1
    return answer