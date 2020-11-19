def solution(board, moves):
    answer = 0
    Que = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                break
        else:
            continue
        take = board[j][i-1]
        board[j][i-1] = 0
        Que.append(take)
        while len(Que)>=2 and Que[-1] == Que[-2]:
            answer += 2
            Que.pop()
            Que.pop()
    return answer