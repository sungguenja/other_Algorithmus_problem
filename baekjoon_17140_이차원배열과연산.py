from copy import deepcopy
r,c,k = map(int,input().split())
A_matrix = [list(map(int,input().split())) for i in range(3)]
answer = 101
cnt = 0
for t in range(101):
    if r<=len(A_matrix) and c<=len(A_matrix[0]) and A_matrix[r-1][c-1] == k:
        answer = cnt
    if answer != 101:
        break
    before_A = deepcopy(A_matrix)
    if len(A_matrix) >= len(A_matrix[0]):
        A_matrix = [[] for i in range(len(before_A))]
        maximum_len = 0
        for i in range(len(before_A)):
            check = [0]*(max(before_A[i]))
            for j in range(len(before_A[i])):
                if before_A[i][j] == 0:
                    continue
                check[before_A[i][j]-1] += 1
            horizon = []
            for j in range(len(check)):
                if check[j] != 0:
                    horizon.append([j+1,check[j]])
            horizon.sort(key=lambda x: (x[1],x[0]))
            for j in range(len(horizon)):
                A_matrix[i].append(horizon[j][0])
                A_matrix[i].append(horizon[j][1])
            if len(A_matrix[i]) > maximum_len:
                maximum_len = len(A_matrix[i])
        for i in range(len(A_matrix)):
            while len(A_matrix[i])<maximum_len:
                A_matrix[i].append(0)
    else:
        A_matrix = [[0]*len(before_A[0]) for i in range(len(before_A)*2)]
        maximum_len = 0
        for j in range(len(before_A[0])):
            check = []
            for i in range(len(before_A)):
                if before_A[i][j] == 0:
                    continue
                for l in range(len(check)):
                    if check[l][0] == before_A[i][j]:
                        check[l][1] += 1
                        break
                else:
                    check.append([before_A[i][j],1])
            check.sort(key=lambda x: (x[1],x[0]))
            for l in range(len(check)):
                A_matrix[2*l][j] = check[l][0]
                A_matrix[2*l+1][j] = check[l][1]
        for i in range(len(A_matrix)):
            
            if A_matrix[i].count(0) == len(A_matrix[i]):
                A_matrix = deepcopy(A_matrix[:i])
                break
    cnt+=1
if answer >= 101:
    print(-1)
else:
    print(answer)