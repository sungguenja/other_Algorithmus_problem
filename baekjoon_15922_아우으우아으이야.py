N = int(input())
x,y = map(int,input().split())
answer = 0

for _ in range(N-1):
    tmp_x,tmp_y = map(int,input().split())
    if x <= tmp_y <= y:
        continue
    elif x <= tmp_x <= y and tmp_y > y:
        y = tmp_y
    else:
        answer += y - x
        x = tmp_x
        y = tmp_y

answer += y - x

print(answer)