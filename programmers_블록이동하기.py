import sys
direction = [[1,1,0,0],[0,0,1,1],[-1,-1,0,0],[0,0,-1,-1],[1,0,1,0],[0,-1,1,0],[0,1,1,0],[0,1,0,1]]
def solution(board):
    visit = [[0,1,0,0,'-']]
    answer = sys.maxsize
    que = [[0,1,0,0,'-',0]]
    while que != []:
        now = que.pop(0)
        x_l,x_r,y_b,y_h,shape,day = now[0],now[1],now[2],now[3],now[4],now[5]
        if (x_l==len(board)-1 or x_r==len(board)-1) and (y_b==len(board)-1 or y_h==len(board)-1):
            if answer > day:
                answer = day
            continue

        for k in direction:
            if shape=='|' and (k==[1,0,1,0] or k==[0,-1,1,0]):
                continue
            if shape=='-' and (k==[0,1,0,1] or k==[0,1,1,0]):
                continue
            nx_l = x_l+k[0]
            nx_r = x_r+k[1]
            ny_b = y_b+k[2]
            ny_h = y_h+k[3]
            if 0<=nx_l<len(board) and 0<=nx_r<len(board) and 0<=ny_b<len(board) and 0<=ny_h<len(board):
                if k!=[1,0,1,0] or k!=[0,1,0,1]:
                    if board[nx_l][ny_b] == 0 and board[nx_l][ny_h] == 0 and board[nx_r][ny_b] == 0 and board[nx_r][ny_h] == 0 and [nx_l,nx_r,ny_b,ny_h,shape] not in visit:
                        que.append([nx_l,nx_r,ny_b,ny_h,shape,day+1])
                        visit.append([nx_l,nx_r,ny_b,ny_h,shape])
                elif k==[1,0,1,0] or k==[0,-1,1,0]:
                    if board[nx_l][ny_b] == 0 and board[nx_l][ny_h] == 0 and board[nx_r][ny_b] == 0 and board[nx_r][ny_h] == 0 and [nx_l,nx_r,ny_b,ny_h,'|'] not in visit:
                        que.append([nx_l,nx_r,ny_b,ny_h,'|',day+1])
                        visit.append([nx_l,nx_r,ny_b,ny_h,'|'])
                elif k==[0,1,0,1] or k==[0,1,1,0]:
                    if board[nx_l][ny_b] == 0 and board[nx_l][ny_h] == 0 and board[nx_r][ny_b] == 0 and board[nx_r][ny_h] == 0 and [nx_l,nx_r,ny_b,ny_h,'-'] not in visit:
                        que.append([nx_l,nx_r,ny_b,ny_h,'-',day+1])
                        visit.append([nx_l,nx_r,ny_b,ny_h,'-'])

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))