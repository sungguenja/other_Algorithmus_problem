def makeList(weights,head2head,N):
    result = []
    for i in range(N):
        win = 0
        bigger = 0
        for j in range(N):
            if (head2head[i][j] == 'W'):
                win += 1
                if weights[i] < weights[j]:
                    bigger += 1
        result.append((win/(N-1),bigger,weights[i],i+1))
    return result

def solution(weights, head2head):
    result = makeList(weights,head2head,len(head2head))
    result.sort(key=lambda x : (-x[0],-x[1],-x[2],x[3]))
    answer = []
    for i in result:
        answer.append(i[3])
    return answer