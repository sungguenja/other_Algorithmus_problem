def entryNeedMoney(price, count):
    result = count * (count+1) * price // 2

    return result

def solution(price, money, count):
    answer = entryNeedMoney(price,count) - money

    if answer <= 0:
        return 0
        
    return answer