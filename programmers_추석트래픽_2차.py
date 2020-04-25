def solution(lines):
    traffic = [0]*len(lines)
    # 시작과 끝을 저장하기 위한 작업
    for i in range(len(lines)):
        this_traffic = lines[i].split()
        last = int(this_traffic[1][:2])*3600000 + int(this_traffic[1][3:5])*60000 + int(this_traffic[1][6:8])*1000 + int(this_traffic[1][9:])
        start = last - int(float(this_traffic[2][:-1])*1000) + 1
        traffic[i] = [start,last]

    maximum_counting = -1
    for i in range(len(traffic)):
        counting = 0
        # i의 시작점 기준으로 시작점 또는 시작점의 1초후 또는 j의 시작점이 i의 시작점과 시작점으로부터 1초 사이에 있으면 카운팅이 가능하다
        for j in range(len(traffic)):
            if traffic[j][0]<=traffic[i][0]<=traffic[j][1] or traffic[j][0]<=traffic[i][0]+999<=traffic[j][1] or traffic[i][0]<=traffic[j][0]<=traffic[i][0]+999:
                counting+=1
        if maximum_counting<counting:
                maximum_counting = counting
        # i의 끝점을 기준으로 위와 상황은 동일
        counting = 0
        for j in range(len(traffic)):
            if traffic[j][0]<=traffic[i][1]<=traffic[j][1] or traffic[j][0]<=traffic[i][1]+999<=traffic[j][1] or traffic[i][1]<=traffic[j][0]<=traffic[i][1]+999:
                counting+=1
            if maximum_counting<counting:
                maximum_counting = counting
    
    return maximum_counting