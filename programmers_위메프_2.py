def solution(N,M,arr):
    answer = N**2 + M**2
    point = []
    for i in range(N):
        if not 1 in arr[i]:
            continue
        for j in range(M):
            if arr[i][j] == 1:
                point.append([i,j])
    if len(point) >= 2:
        for i in range(len(point)-1):
            for j in range(i+1,len(point)):
                if answer > round(((point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2)**(1/2,2)):
                    answer = round(((point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2)**(1/2,2))
                if answer == 1.0:
                    break
            if answer == 1.0:
                break
    else:
        answer = 0.0
    return answer