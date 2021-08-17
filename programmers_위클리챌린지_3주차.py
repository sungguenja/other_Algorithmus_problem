from collections import deque
from copy import deepcopy
def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])

    result = [[0]*n for i in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = matrix[i][j]
    
    return result

def makeRectangle(arr):
    max_i = -1
    max_j = -1
    min_i = 60
    min_j = 60
    for tu in arr:
        if min_i > tu[0]:
            min_i = tu[0]
        if max_i < tu[0]:
            max_i = tu[0]
        if min_j > tu[1]:
            min_j = tu[1]
        if max_j < tu[1]:
            max_j = tu[1]
    
    blank_matrix = [[0]*(max_j-min_j+1) for i in range(max_i-min_i+1)]
    for tu in arr:
        blank_matrix[tu[0]-min_i][tu[1]-min_j] = 1
    
    return blank_matrix

def bfs(i,j,value,board):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visit = [(i,j)]
    Que = deque()
    Que.append((i,j))
    while Que:
        now_i,now_j = Que.popleft()
        for k in range(4):
            ni = now_i + di[k]
            nj = now_j + dj[k]
            if 0<=ni<len(board) and 0<=nj<len(board[ni]):
                if board[ni][nj] == value and (ni,nj) not in visit:
                    visit.append((ni,nj))
                    Que.append((ni,nj))
    
    return visit,makeRectangle(visit)

def solution(game_board, table):
    blank_point_list = []
    visit = [[False]*len(game_board[0]) for i in range(len(game_board))]
    answer = 0
    table_visit = [[False]*len(table[0]) for i in range(len(table))]
    table_point_list = []
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                visit[i][j] = True
            elif game_board[i][j] == 0 and not visit[i][j]:
                bfs_visit,bfs_blank_matrix = bfs(i,j,game_board[i][j],game_board)
                for vi in bfs_visit:
                    visit[vi[0]][vi[1]] = True
                blank_point_list.append(deepcopy(bfs_blank_matrix))
            
            if table[i][j] == 1 and not table_visit[i][j]:
                bfs_visit,bfs_blank_matrix = bfs(i,j,table[i][j],table)
                for vi in bfs_visit:
                    table_visit[vi[0]][vi[1]] = True
                table_point_list.append(deepcopy(bfs_blank_matrix))
            elif table[i][j] == 0:
                table_visit[i][j] = True
    
    table_point_list_visit = [False]*len(table_point_list)
    for i in range(len(blank_point_list)):
        before_answer = answer
        for j in range(len(table_point_list)):
            if not table_point_list_visit[j]:
                for k in range(4):
                    if not (len(blank_point_list[i]) == len(table_point_list[j]) and len(blank_point_list[i][0]) == len(table_point_list[j][0])):
                        table_point_list[j] = rotate(table_point_list[j])
                        continue
                    trigger = False
                    inner_cnt = 0
                    for u in range(len(table_point_list[j])):
                        for v in range(len(table_point_list[j][u])):
                            if table_point_list[j][u][v] == blank_point_list[i][u][v]:
                                if table_point_list[j][u][v] == 1:
                                    inner_cnt += 1
                            else:
                                trigger = True
                                break
                        if trigger:
                            break
                    
                    if trigger:
                        table_point_list[j] = rotate(table_point_list[j])
                    else:
                        table_point_list_visit[j] = True
                        answer += inner_cnt
                        break
            if before_answer != answer:
                break

    return answer
