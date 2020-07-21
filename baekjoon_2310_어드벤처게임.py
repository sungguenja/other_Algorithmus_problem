def solution(arr,whe=0,cost=0):
    global answer
    if cost<0:
        return
    
    if whe == len(arr) and cost>=0:
        answer = 'Yes'
        return

    if answer == 'No':
        if whe != len(arr)-1:
            for i in range(2,len(arr[whe])-1):
                if visit[arr[whe][i]-1] == 0:
                    visit[arr[whe][i]-1] = 1
                    if arr[whe][0] == 'E':
                        solution(arr,arr[whe][i]-1,cost)
                    elif arr[whe][0] == 'L':
                        if cost<arr[whe][1]:
                            solution(arr,arr[whe][i]-1,arr[whe][1])
                        else:
                            solution(arr,arr[whe][i]-1,cost)
                    elif arr[whe][0] == 'T':
                        solution(arr,arr[whe][i]-1,cost-arr[whe][1])
                    visit[arr[whe][i]-1] = 0
        else:
            if arr[whe][0] == 'E' or arr[whe][0] == 'L':
                solution(arr,len(arr),cost)
            else:
                if cost>=arr[whe][1]:
                    solution(arr,len(arr),cost)
                else:
                    return


N = int(input())
while N != 0:
    room = [0]*N
    for i in range(N):
        room[i] = list(input().split())
        for j in range(len(room[i])):
            if j==0:
                continue
            else:
                room[i][j] = int(room[i][j])
    visit = [0]*N
    answer = 'No'
    solution(room)
    print(answer)
    N = int(input())