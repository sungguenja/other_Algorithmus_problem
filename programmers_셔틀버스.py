def solution(n, t, m, timetable):
    hour = 9
    minute = 0
    timetable = sorted(timetable)
    cnt = 0
    for i in range(n):
        if i!=0:
            minute += t
            if minute>=60:
                hour += 1
                minute -= 60
        now = 0
        for j in range(m):
            person_hour = int(timetable[cnt][0:2])
            person_minu = int(timetable[cnt][3:5])
            if person_hour<hour:
                cnt += 1
                now += 1
            elif person_hour == hour:
                if person_minu <= minute:
                    cnt += 1
                    now += 1
                else:
                    break
            else:
                break
            if now == m or cnt>=len(timetable):
                break
    if now == m:
        minute += t
        if minute >= 60:
            hour += 1
            minute -= 60
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    answer = hour + ':' + minute
    return answer

print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))