def solution(k,room_number):
    room = {}
    answer = []
    for i in range(len(room_number)):
        now_room = room.get(room_number[i])
        if now_room == None:
            room[room_number[i]] = room_number[i]+1
            answer.append(room_number[i])
        else:
            z = room[room_number[i]]
            while room.get(z) != None:
                bz = z
                z = room.get(z)
                if room.get(z) != None:
                    room[bz] = room[z]
            answer.append(z)
            room[z] = z+1
    return answer