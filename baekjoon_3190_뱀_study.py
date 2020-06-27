direction = [[0,1],[1,0],[0,-1],[-1,0]]
N=int(input())
apple_cnt = int(input())
apple = [0]*apple_cnt
for i in range(apple_cnt):
    apple[i] = list(map(int,input().split()))
commend_cnt = int(input())
commend = [0]*commend_cnt
for i in range(commend_cnt):
    commend[i] = list(input().split())
    commend[i][0] = int(commend[i][0])

cnt=0
snake = [[1,1]]
way = 0
commend_cnt = 0
while True:
    cnt+=1
    head = snake[0][:]
    tail = snake[-1][:]
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다
    head[0] = head[0]+direction[way][0]
    head[1] = head[1]+direction[way][1]
    # 머리가 먼저 늘어나고 꼬리가 늦게 빠지기에 죽는 경우임
    if head == tail:
        break
    # 머리가 몸안으로 들어갈 때
    elif head in snake[1:]:
        break
    if head[0]>N or head[0]<=0 or head[1]>N or head[1]<=0:
        break
    # 만약 다음칸에 사과가 있다면
    if head in apple:
        snake.append(tail)
        apple.pop(apple.index(head))
    # 이동
    for i in range(len(snake)-1,0,-1):
        snake[i] = snake[i-1][:]
    snake[0] = head[:]
    # 방향 틀기
    if commend_cnt!=len(commend):
        if cnt == commend[commend_cnt][0]:
            if commend[commend_cnt][1] == 'L':
                way -= 1
                if way == -1:
                    way = 3
            elif commend[commend_cnt][1] == 'D':
                way += 1
                if way == 4:
                    way = 0
            commend_cnt += 1
print(cnt)