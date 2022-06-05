N = int(input())
answer = 0
stack = [0]

for i in range(N):
    X,Y = map(int,input().split())
    if stack[-1] < Y:
        answer += 1
        stack.append(Y)
    else:
        while stack[-1] > Y:
            stack.pop()
        
        if stack[-1] < Y:
            answer += 1
            stack.append(Y)

print(answer)