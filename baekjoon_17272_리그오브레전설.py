from sys import stdin
input = stdin.readline

mod = 1000000007

def matrixPowerModular(base,size,power):
    answer = [[0] * size for _ in range(size)]
    for i in range(size):
        answer[i][i] = 1
    
    while power:
        if (power % 2):
            answer = matrixApply(answer, base, size)
        base = matrixApply(base,base,size)
        power = power // 2
    
    return answer

def matrixApply(matrixA, matrixB, size):
    answer = [[0] * size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            for j in range(size):
                tmp = matrixA[i][k] * matrixB[k][j] % mod
                answer[i][j] = (answer[i][j] + tmp) % mod
    return answer


def coolTime(N,M):
    if (N < M):
        return 1
    
    if (N == M):
        return 2
    
    if (N == M+1):
        return 3
    
    size = M + 1
    power = N - M - 1

    base = [[0] * size for _ in range(size)]
    for i in range(0,size-1):
        base[i][i+1] = 1
    base[size-1][1] = 1
    base[size-1][size-1] = 1

    base = matrixPowerModular(base, size, power)
    
    answer = 0

    for i in range(size-2):
        answer = (answer + base[size-1][i]) % mod
    answer = (answer + base[size-1][size-2] * 2) % mod
    answer = (answer + base[size-1][size-1] * 3) % mod

    return answer



N,M = map(int,input().split())

print(coolTime(N,M))