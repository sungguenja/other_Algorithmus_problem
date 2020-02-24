def solution(N):
    area = [0,4,6]
    if N+1>len(area):
        for i in range(3,N+1):
            area.append(area[i-1]+area[i-2])
    return area[N]