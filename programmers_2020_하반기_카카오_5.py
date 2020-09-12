def solution(play_time, adv_time, logs):
    answer = ''
    end_time = int(play_time[0:2])*3600 + int(play_time[3:5])*60 + int(play_time[6:])
    adv_long = int(adv_time[0:2])*3600 + int(adv_time[3:5])*60 + int(adv_time[6:])
    sec_log = [[int(logs[i][0:2])*3600 + int(logs[i][3:5])*60 + int(logs[i][6:8]),int(logs[i][9:11])*3600 + int(logs[i][12:14])*60 + int(logs[i][15:])] for i in range(len(logs))]
    start_time = 0
    adv_count = -1
    start_case = [i[0] for i in sec_log]
    start_case.append(0)
    for i in range(end_time):
        adv_start_time = i
        adv_end_time = i+adv_long
        if adv_end_time>end_time:
            break
        now_adv_count = 0
        for j in range(len(sec_log)):
            if adv_start_time<=sec_log[j][0]<=adv_end_time or sec_log[j][0]<=adv_start_time<=sec_log[j][1] or (adv_start_time<=sec_log[j][0]<=sec_log[j][1]<=adv_end_time):
                if sec_log[j][0]>adv_start_time:
                    if sec_log[j][1]>adv_end_time:
                        now_adv_count += adv_end_time-sec_log[j][0]
                    else:
                        now_adv_count += sec_log[j][1]-sec_log[j][0]
                else:
                    if sec_log[j][1]>adv_end_time:
                        now_adv_count += adv_end_time-adv_start_time
                    else:
                        now_adv_count += sec_log[j][1]-adv_start_time
        if now_adv_count > adv_count:
            adv_count = now_adv_count
            start_time = adv_start_time
    hour = str(start_time//3600)
    start_time %= 3600
    minute = str(start_time//60)
    start_time %= 60
    sec = str(start_time)
    if len(hour) < 2:
        hour = '0'+hour
    if len(minute) < 2:
        minute = '0'+minute
    if len(sec) < 2:
        sec = '0'+sec
    answer = hour + ':' + minute + ':' + sec
    return answer
print(solution('99:59:59',"25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))