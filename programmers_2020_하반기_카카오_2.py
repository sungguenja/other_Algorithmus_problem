from itertools import combinations
def solution(orders, course):
    trigger = False
    maximum_len = 0
    menus = {}
    menu = []     
    for i in range(len(orders)):
        if trigger:
            break
        if len(orders[i])>maximum_len:
            maximum_len = len(orders[i])
        for j in range(len(orders[i])):
            if menus.get(orders[i][j]) == None:
                menus[orders[i][j]] = 1
            elif menus.get(orders[i][j]) == 1:
                menus[orders[i][j]] += 1
                menu.append(orders[i][j])
    order_case = {i:0 for i in course}
    menu.sort()
    for i in course:
        if i>maximum_len:
            break
        menu_case = list(combinations(menu,i))
        for j in menu_case:
            cnt = 0
            for l in orders:
                if len(l) < len(j):
                    continue
                for m in j:
                    if m in l:
                        continue
                    else:
                        break
                else:
                    cnt+=1
            if cnt>=2:
                if order_case[i] == 0:
                    order_case[i] = [[j,cnt]]
                else:
                    if cnt>order_case[i][0][1]:
                        order_case[i] = [[j,cnt]]
                    elif cnt == order_case[i][0][1]:
                        order_case[i].append([j,cnt])
    answer = []
    for i in order_case.values():
        if i==0:
            continue
        for j in i:
            answer.append(''.join(j[0]))
    answer.sort()
    return answer
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
