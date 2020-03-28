def solution(k,room_number):
    room = [0]*(k+1)
    answer = []
    for i in range(len(room_number)):
        if room[room_number[i]] == 0:
            answer.append(room_number[i])
            room[room_number[i]] = 1
        else:
            z=room[room_number[i]:].index(0)
            answer.append(z)
            room[z] = 1
    return answer