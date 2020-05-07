def solution(routes):
    routes.sort(key=lambda x:x[1])
    now_camera = routes[0][1]
    answer = 1
    for i in range(len(routes)):
        if now_camera<routes[i][0]:
            answer+=1
            now_camera = routes[i][1]
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))