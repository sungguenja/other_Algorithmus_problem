direction = [[0,1],[1,0],[0,-1],[-1,0]]
def solution(N,M,guide):
    answer = ''
    visit = [[False]*M for i in range(N)]
    answer_dict = dict()
    for i in range(26):
        answer_dict[chr(i+65)] = None
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and guide[i][j] != '*':
                que = [[i,j]]
                visit[i][j] = True
                arr = [0]*26
                if guide[i][j] != '-':
                    arr[ord(guide[i][j])-65] += 1
                while que != []:
                    ni,nj = que.pop(0)
                    if guide[ni][nj] != '-' and answer_dict[guide[ni][nj]] == None:
                        answer_dict[guide[ni][nj]] = 0
                    for k in direction:
                        nni = ni+k[0]
                        nnj = nj+k[1]
                        if 0<=nni<N and 0<=nnj<M and guide[nni][nnj] != '*' and not visit[nni][nnj]:
                            que.append([nni,nnj])
                            visit[nni][nnj] = True
                            if guide[nni][nnj] != '-':
                                arr[ord(guide[nni][nnj])-65] += 1
                maximum = max(arr)
                if maximum != 0:
                    answer_dict[chr(arr.index(maximum)+65)] += maximum
    for key, value in answer_dict.items():
        if value == None:
            continue
        answer += key+str(value)
    return answer