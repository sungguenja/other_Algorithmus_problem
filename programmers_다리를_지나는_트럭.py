def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    while bridge != [] or truck_weights != []:
        print(answer,bridge,truck_weights)
        answer += 1
        bridge_weight = 0
        for i in range(len(bridge)):
            bridge[i][1] += 1
        if bridge != [] and bridge[0][1] == bridge_length:
            bridge.pop(0)
        for i in range(len(bridge)):
            bridge_weight += bridge[i][0]
        if truck_weights != [] and bridge_weight+truck_weights[0]<=weight:
            bridge.append([truck_weights.pop(0),0])
    return answer

print(solution(2,10,[7,4,5,6]))