from collections import deque
direction = [[1,0],[0,1],[-1,0],[0,-1]]
def solution(board):
    answer = -1
    N = len(board)
    Que = deque()
    Que.append([[[0,0],[0,1]],0])
    visit=[[[0,0],[0,1]]]
    while len(Que) != 0:
        robot,cnt = Que.popleft()
        if [N-1,N-1] in robot:
            if answer == -1 or answer>cnt:
                answer = cnt
            continue
        robot_1 = robot[0][:]
        robot_2 = robot[1][:]
        for k in direction:
            r1ni = robot_1[0] + k[0]
            r1nj = robot_1[1] + k[1]
            r2ni = robot_2[0] + k[0]
            r2nj = robot_2[1] + k[1]
            if 0<=r1ni<N and 0<=r1nj<N and 0<=r2ni<N and 0<=r2nj<N:
                if sorted([[r1ni,r1nj],[r2ni,r2nj]]) not in visit and board[r1ni][r1nj] == 0 and board[r2ni][r2nj] == 0:
                    visit.append(sorted([[r1ni,r1nj],[r2ni,r2nj]]))
                    Que.append([sorted([[r1ni,r1nj],[r2ni,r2nj]]),cnt+1])
        # 가로방향 회전
        if robot_1[0] == robot_2[0]:
            r1ni = robot_1[0]
            r1nj = robot_1[1]
            r2ni = robot_2[0]
            r2nj = robot_2[1]
            # 아래 두곳 확인
            if 0<=r1ni+1<N and 0<=r1nj<N and 0<=r2ni+1<N and 0<=r2nj<N:
                if board[r1ni+1][r1nj]==0 and board[r2ni+1][r2nj]==0:
                    if sorted([[r1ni+1,r1nj+1],[r2ni,r2nj]]) not in visit and 0<=r1nj+1<N:
                        visit.append(sorted([[r1ni+1,r1nj+1],[r2ni,r2nj]]))
                        Que.append([sorted([[r1ni+1,r1nj+1],[r2ni,r2nj]]),cnt+1])
                    if sorted([[r1ni,r1nj],[r2ni+1,r2nj-1]]) not in visit and 0<=r2nj-1<N:
                        visit.append(sorted([[r1ni,r1nj],[r2ni+1,r2nj-1]]))
                        Que.append([sorted([[r1ni,r1nj],[r2ni+1,r2nj-1]]),cnt+1])
            # 위 두곳 확인
            if 0<=r1ni-1<N and 0<=r1nj<N and 0<=r2ni-1<N and 0<=r2nj<N:
                if board[r1ni-1][r1nj]==0 and board[r2ni-1][r2nj]==0:
                    if sorted([[r1ni-1,r1nj+1],[r2ni,r2nj]]) not in visit and 0<=r1nj+1<N:
                        visit.append(sorted([[r1ni-1,r1nj+1],[r2ni,r2nj]]))
                        Que.append([sorted([[r1ni-1,r1nj+1],[r2ni,r2nj]]),cnt+1])
                    if sorted([[r1ni,r1nj],[r2ni-1,r2nj-1]]) not in visit and 0<=r2nj-1<N:
                        visit.append(sorted([[r1ni,r1nj],[r2ni-1,r2nj-1]]))
                        Que.append([sorted([[r1ni,r1nj],[r2ni-1,r2nj-1]]),cnt+1])
        # 세로방향 회정
        else:
            r1ni = robot_1[0]
            r1nj = robot_1[1]
            r2ni = robot_2[0]
            r2nj = robot_2[1]
            # 왼쪽 두곳 확인
            if 0<=r1ni<N and 0<=r1nj-1<N and 0<=r2ni<N and 0<=r2nj-1<N:
                if board[r1ni][r1nj-1]==0 and board[r2ni][r2nj-1]==0:
                    if sorted([[r1ni+1,r1nj-1],[r2ni,r2nj]]) not in visit and 0<=r1ni+1<N:
                        visit.append(sorted([[r1ni+1,r1nj-1],[r2ni,r2nj]]))
                        Que.append([sorted([[r1ni+1,r1nj-1],[r2ni,r2nj]]),cnt+1])
                    if sorted([[r1ni,r1nj],[r2ni-1,r2nj-1]]) not in visit and 0<=r2ni-1<N:
                        visit.append(sorted([[r1ni,r1nj],[r2ni-1,r2nj-1]]))
                        Que.append([sorted([[r1ni,r1nj],[r2ni-1,r2nj-1]]),cnt+1])
            # 오른쪽 두곳 확인
            if 0<=r1ni<N and 0<=r1nj+1<N and 0<=r2ni<N and 0<=r2nj+1<N:
                if board[r1ni][r1nj+1]==0 and board[r2ni][r2nj+1]==0:
                    if sorted([[r1ni+1,r1nj+1],[r2ni,r2nj]]) not in visit and 0<=r1ni+1<N:
                        visit.append(sorted([[r1ni+1,r1nj+1],[r2ni,r2nj]]))
                        Que.append([sorted([[r1ni+1,r1nj+1],[r2ni,r2nj]]),cnt+1])
                    if sorted([[r1ni,r1nj],[r2ni-1,r2nj+1]]) not in visit and 0<=r2ni-1<N:
                        visit.append(sorted([[r1ni,r1nj],[r2ni-1,r2nj+1]]))
                        Que.append([sorted([[r1ni,r1nj],[r2ni-1,r2nj+1]]),cnt+1])
    return answer

print(solution(	[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))