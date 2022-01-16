def makeMinute(time_arr):
    min_minute = 24*60
    minute_arr = []
    for i in range(len(time_arr)):
        hour,minute = time_arr[i].split(':')
        now_time = int(hour) * 60 + int(minute)
        if now_time < min_minute:
            min_minute = now_time
        minute_arr.append(now_time)
    minute_arr.sort()
    return minute_arr, min_minute

def makeBusTable(n,t):
    now_time = 9*60
    bus_table = []
    for i in range(n):
        bus_table.append(now_time + i * t)
    return bus_table

def makeTime(minute):
    answer = ''
    if minute // 60 < 10:
        answer += '0' + str(minute//60) + ':'
    else:
        answer = str(minute//60) + ':'
    if minute % 60 < 10:
        answer += '0' + str(minute%60)
    else:
        answer += str(minute%60)
    return answer

def solution(n, t, m, timetable):
    answer = ''
    length = len(timetable)
    new_timetable, min_minute = makeMinute(timetable)
    visit = [-1]*length
    bus_table = makeBusTable(n,t)
    bus_diction = {}
    for i in range(n):
        for j in range(length):
            if new_timetable[j] <= bus_table[i]:
                if visit[j] == -1:
                    if bus_diction.get(bus_table[i]) == None:
                        bus_diction[bus_table[i]] = [new_timetable[j]]
                        visit[j] = 1
                    else:
                        if len(bus_diction[bus_table[i]]) < m:
                            bus_diction[bus_table[i]].append(new_timetable[j])
                            visit[j] = 1
                        else:
                            visit[j] = 0
                elif visit[j] == 0:
                    if bus_diction.get(bus_table[i]) == None:
                        bus_diction[bus_table[i]] = [new_timetable[j]]
                        visit[j] = 1
                    elif len(bus_diction[bus_table[i]]) < m:
                        bus_diction[bus_table[i]].append(new_timetable[j])
                        visit[j] = 1
    last_bus_member = bus_diction.get(bus_table[-1])
    if last_bus_member == None or len(last_bus_member) < m:
        answer = makeTime(bus_table[-1])
    else:
        if len(set(last_bus_member)) == 1: 
            answer = makeTime(min(last_bus_member)-1)
        else:
            answer = makeTime(max(last_bus_member)-1)
    return answer