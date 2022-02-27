def solution(n, results):
    answer = 0
    winner_dict = {key:set() for key in range(1,n+1)} # key에게 이긴 사람들
    loser_dict = {key:set() for key in range(1,n+1)} # key에게 진 사람들
    
    for winner,loser in results:
        winner_dict[loser].add(winner)
        loser_dict[winner].add(loser)
    
    for i in range(1,n+1):
        for winner in winner_dict[i]:
            loser_dict[winner].update(loser_dict[i])
        for loser in loser_dict[i]:
            winner_dict[loser].update(winner_dict[i])
    
    for i in range(1,n+1):
        if len(winner_dict[i]) + len(loser_dict[i]) == n-1:
            answer+=1
    return answer