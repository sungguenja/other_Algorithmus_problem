def solution(gems):
    answer = []
    gem_arr = set(gems)
    trigger = False
    if len(gem_arr) != 1:
        for i in range(len(gems)):
            for j in gem_arr:
                if gems[i:].count(j) == 0:
                    trigger = True
                    break
            if trigger:
                break
        save_i = i
        trigger = False
        for i in range(len(gems)-1,-1,-1):
            for j in gem_arr:
                if gems[:i].count(j) == 0:
                    trigger =True
                    break
            if trigger:
                break
        save_j = i
        print(save_i,save_j)
        if save_i>save_j:
            save_i,save_j = save_j,save_i
        elif save_i==save_j:
            save_i-=1
        save_j+=1

        answer = [save_i,save_j]
    else:
        answer = [1,1]
    return answer

print(solution(["AA", "AB", "AC", "AA", "AC"]))