def solution(lines):
    traffic = [0]*len(lines)
    for i in range(len(lines)):
        Z = lines[i].split()
        complete = int(Z[1][:2])*3600000 + int(Z[1][3:5])*60000 + int(Z[1][6:8])*1000 + int(Z[1][9:])
        consume = int(float(Z[2][:-1])*1000)
        traffic[i] = [complete-consume+1,complete]

    counting = 0
    for k in range(len(traffic)):
        now_count = 0
        for j in range(len(traffic)):
            if traffic[j][0]<=traffic[k][0]<=traffic[j][1] or traffic[j][0]<=traffic[k][0]+999<=traffic[j][1]:
                now_count += 1
        if now_count>counting:
            counting = now_count
        now_count = 0
        for j in range(len(traffic)):
            if traffic[j][0]<=traffic[k][1]<=traffic[j][1] or traffic[j][0]<=traffic[k][1]+999<=traffic[j][1]:
                now_count += 1
        if now_count>counting:
            counting = now_count

    return counting

X=['2016-09-15 01:00:04.001 2.0s','2016-09-15 01:00:07.000 2s']
print(solution(X))