chess = {}
answer = 'Valid'
before_location = ''
direction = [[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2]]
alphabet = ['A','B','C','D','E','F']
number = ['1','2','3','4','5','6']
now = 3
goal = ''
for i in range(36):
    location = str(input())
    if before_location != '':
        x = ord(before_location[0])-ord(location[0])
        y = int(before_location[1])-int(location[1])
        if [x,y] not in direction:
            answer = 'Invalid'
        if (before_location[0] == 'A' and (location[0] == 'F' or location[0] == 'E')) or (before_location[0] == 'B' and location[0] == 'F'):
            answer = 'Invalid'
        if (before_location[1] == '1' and (location[1] == '6' or location[1] == '5')) or (before_location[1] == '2' and location[1] == '6'):
            answer = 'Invalid'
    else:
        goal = location
    if location[0] not in alphabet or location[1] not in number:
        answer = 'Invalid'
    if chess.get(location) == None:
        chess[location] = 1
    else:
        chess[location] += 1
        answer = 'Invalid'
    before_location = location
x = ord(location[0]) - ord(goal[0])
y = int(location[1]) - int(goal[1])
if [x,y] not in direction:
    answer = 'Invalid'
if len(chess.keys()) != 36:
    answer = 'Invalid'
print(answer)