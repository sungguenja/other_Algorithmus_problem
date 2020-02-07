N,M = map(int, input().split())
start_link = []
for _ in range(N):
    vertical = []
    vertical = list(input())
    start_link.append(vertical)

dk=[[0,1],[1,0],[0,-1],[-1,0]]

for i in range(N):
    for j in range(M):
        if start_link[i][j] == 'R':
            red = [i,j]
        if start_link[i][j] == 'B':
            blue = [i,j]
        if start_link[i][j] == 'O':
            hole = [i,j]

result = 0
stack = [1]
movement = 0
b=0
stuck = 0
no_goal = 0
while not result:
    for k in range(len(dk)):
        if stuck == 3:
            stuck = 0
            stack.pop()
            stack.append(1)

        if dk[k] in stack:
            stuck += 1
            continue

        if [blue[0]+dk[k][0],blue[1]+dk[k][1]] == hole or blue == hole:
            result = 1
            no_goal = 'no goal'
        
        if [red[0]+dk[k][0],red[1]+dk[k][1]] == hole or red == hole:
            result = 1

        if start_link[red[0]+dk[k][0]][red[1]+dk[k][1]] == '.':
            start_link[red[0]][red[1]] = '.'
            start_link[blue[0]][blue[1]] = '.'
            while start_link[red[0]+dk[k][0]][red[1]+dk[k][1]] == '.' or start_link[red[0]+dk[k][0]][red[1]+dk[k][1]] == 'O':
                red[0] += dk[k][0]
                red[1] += dk[k][1]
            while start_link[blue[0]+dk[k][0]][blue[1]+dk[k][1]] == '.' or start_link[blue[0]+dk[k][0]][blue[1]+dk[k][1]] == 'O':
                blue[0] += dk[k][0]
                blue[1] += dk[k][1]
            if red == blue:
                blue[0] -= dk[k][0]
                blue[1] -= dk[k][1]
            start_link[red[0]][red[1]] = 'R'
            start_link[blue[0]][blue[1]] = 'B'
            movement += 1
            stack.pop()
            stack.append(dk[k-2])
        if movement > 10:
            result = 1
            no_goal = 'no goal'
            break

if no_goal==0:
    print(1)
else:
    print(0)