def solution(N, simulation_data):
    answer = 0
    counselor = [0]*N
    time = 0
    while simulation_data != []:
        
        for i in range(N):
            if counselor[i] != 0:
                counselor[i][2] += 1
                if counselor[i][2]>=counselor[i][1]:
                    counselor[i]=0
    
        if time >= simulation_data[0][0]:
            for i in range(N):
                if counselor[i]==0 and (len(simulation_data)!=0 and time>=simulation_data[0][0]):
                    consumer = simulation_data.pop(0)
                    consumer.append(0)
                    counselor[i]=consumer
                    
            else:
                for i in range(len(simulation_data)):
                    if time >= simulation_data[i][0]:
                        answer += 1
                    else:
                        break
        time += 1
    return answer