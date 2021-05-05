class User:
    def __init__(self,status,input_id):
        self.input_id = input_id
        self.status = status

def solution(record):
    answer = []
    nick = {}
    for rec in record:
        command = list(rec.split())
        if len(command) == 3:
            if command[0] == 'Enter':
                answer.append(User(command[0],command[1]))
                nick[command[1]] = command[2]
            else:
                nick[command[1]] = command[2]
        else:
            answer.append(User(command[0],command[1]))

    i = 0        
    for ans in answer:
        if ans.status == 'Enter':
            answer[i] = nick[ans.input_id] + '님이 들어왔습니다.'
        else:
            answer[i] = nick[ans.input_id] + '님이 나갔습니다.'
        i += 1
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))