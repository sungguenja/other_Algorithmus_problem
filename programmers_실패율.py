def solution(N, stages):
    answer = []
    stage_people = [0]*(N+2)
    stage_clear = [0]*(N+2)
    for stage in stages:
        stage_clear[stage-1] += 1
        stage_people[stage] += 1
    stage_state = [0]*N
    for i in range(1,N+1):
        entire_people = sum(stage_people[i:])
        clear_people = stage_clear[i-1]
        if entire_people != 0:
            stage_state[i-1] = (i,(clear_people)/entire_people)
        else:
            stage_state[i-1] = (i,0)
    stage_state.sort(key=lambda x : x[1],reverse=True)
    answer = [i[0] for i in stage_state]
    return answer