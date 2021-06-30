N = int(input())
arr = list(map(int,input().split()))
rank = [0]*N
backtrack = [-1]*N
maximum_length = 0
position = -1
for i in range(N):
    for j in range(i+1,N):
        if arr[i] < arr[j]:
            if rank[j] <= rank[i] + 1:
                rank[j] = rank[i] + 1
                backtrack[j] = i
                if rank[j] > maximum_length:
                    maximum_length = rank[j]
                    position = j


if N != 1:
    print(maximum_length+1)
    status = backtrack[position]
    answer = [-1]*(maximum_length+1)
    while status != -1:
        answer[rank[position]] = str(arr[position])
        position = status
        status = backtrack[position]
    answer[rank[position]] = str(arr[position])
    print(' '.join(answer))
else:
    print(1)
    answer = list(map(str,arr))
    print(' '.join(answer))