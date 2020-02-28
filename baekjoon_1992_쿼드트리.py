def quadtree(n,start_i,start_j):
    color = tv[start_i][start_j]

    for i in range(start_i,start_i+n):
        trigger = 0
        for j in range(start_j,start_j+n):
            if color != tv[i][j]:
                zip_color.append('(')  # 여기서 상황이 달라지니까 여는 괄호 추가
                trigger = 1
                quadtree(n//2,start_i,start_j)
                quadtree(n//2,start_i,start_j+n//2)
                quadtree(n//2,start_i+n//2,start_j)
                quadtree(n//2,start_i+n//2,start_j+n//2)
                zip_color.append(')')   # 달라진 상황이 끝나므로 닫는 괄호 추가
                break
        if trigger==1:
            break
    
    if trigger==0:
        zip_color.append(color)

N=int(input())
zip_color=[]
tv = [list(input()) for _ in range(N)]
quadtree(N,0,0)
print(''.join(zip_color))