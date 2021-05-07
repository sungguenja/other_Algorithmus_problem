import itertools
def solution(orders, course):
    answer = []
    menu_cnt = {}
    order_len = {}
    for i in range(len(orders)):
        order_list = orders[i]
        for now_len in range(len(order_list),1,-1):
            if order_len.get(now_len) == None:
                order_len[now_len] = [order_list]
            else:
                order_len[now_len].append(order_list)
        for order in order_list:
            if menu_cnt.get(order) == None:
                menu_cnt[order] = 1
            else:
                menu_cnt[order] += 1
                
    menu = {key:value for key,value in menu_cnt.items() if value >= 2}
    for cou in course:
        now_combination = itertools.combinations(menu,cou)
        out_cnt = 0
        out_result = []
        for now in now_combination:
            cnt = 0
            for order in order_len[cou]:
                if len(order)<cou:
                    continue
                for alp in now:
                    if alp not in order:
                        break
                else:
                    cnt += 1
            if cnt >= 2:
                if cnt > out_cnt:
                    out_cnt = cnt
                    now = list(now)
                    now.sort()
                    out_result = [''.join(now)]
                elif cnt == out_cnt:
                    now = list(now)
                    now.sort()
                    out_result.append(''.join(now))
        answer.extend(out_result)
    answer.sort()
    return answer