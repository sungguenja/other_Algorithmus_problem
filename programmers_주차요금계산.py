from math import ceil
def makeTimeCostMap(records):
    time_cost = {}
    spend_map = {}
    for record in records:
        time,number,is_in = record.split(" ")
        hour,minute = time.split(":")
        spend_minute = int(hour)*60+int(minute)
        if is_in == "IN":
            time_cost[number] = spend_minute
        else:
            intime = time_cost[number]
            if spend_map.get(number) == None:
                spend_map[number] = spend_minute - intime
            else:
                spend_map[number] += spend_minute - intime
            del time_cost[number]
    maximum_time = 23*60 + 59
    for key in time_cost:
        if spend_map.get(key) == None:
            spend_map[key] = maximum_time - time_cost[key]
        else:
            spend_map[key] += maximum_time - time_cost[key]
    
    return spend_map
            
def solution(fees, records):
    basic_time,basic_fee,time_duration,duration_fee = fees
    time_cost = makeTimeCostMap(records)
    time_list_with_tuple = list(time_cost.items())
    time_list_with_tuple.sort(key=lambda x:int(x[0]))
    answer = []
    for inner_tuple in time_list_with_tuple:
        number, spend_time = inner_tuple
        if spend_time <= basic_time:
            answer.append(basic_fee)
        else:
            money = basic_fee + ceil((spend_time - basic_time)/time_duration)*duration_fee
            answer.append(money)
    return answer