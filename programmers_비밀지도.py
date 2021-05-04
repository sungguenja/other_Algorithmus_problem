def makeBin(n,arr):
    for i in range(len(arr)):
        now_bin = bin(arr[i])[2:]
        while len(now_bin)<n:
            now_bin = '0'+now_bin
        arr[i] = now_bin
    return arr

def solution(n, arr1, arr2):
    answer = []
    arr1 = makeBin(n,arr1)
    arr2 = makeBin(n,arr2)
    print(arr1)
    print(arr2)
    for i in range(n):
        inner_answer = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                inner_answer += '#'
            else:
                inner_answer += ' '
        answer.append(inner_answer)
    return answer