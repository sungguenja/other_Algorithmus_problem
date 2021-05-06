def makeSec(time_string):
    hour,minute,sec = map(int,time_string.split(':'))
    return hour * 3600 + minute * 60 + sec

def makeTime(sec):
    hour = str(sec//3600)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str((sec%3600)//60)
    if len(minute) == 1:
        minute = '0' + minute
    second = str(sec%60)
    if len(second) == 1:
        second = '0' + second
    return hour + ":" + minute + ":" + second

def solution(play_time, adv_time, logs):
    answer = 0
    play_time = makeSec(play_time)
    adv_time = makeSec(adv_time)
    time_list = [0]*(360001)
    for i in range(len(logs)):
        log = logs[i]
        start,end = log.split('-')
        time_list[makeSec(start)] += 1
        time_list[makeSec(end)] -= 1
    for _ in range(2):
        for i in range(1,play_time + 1):
            time_list[i] += time_list[i-1]
    
    answer = 0
    answer_cnt = 0
    i = 0
    while i + adv_time < play_time:
        tmp = time_list[i + adv_time] - time_list[i]
        if tmp > answer_cnt:
            answer_cnt = tmp
            answer = i + 1
        i += 1
    answer = makeTime(answer)
    return answer