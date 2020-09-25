def solution(N):
    if N < 3:
        return memo[N]
    elif N >= 3:
        if N<len(memo):
            return memo[N]
        else:
            memo.append(solution(N-1)+solution(N-2))
            return memo[N]
memo = [0,1,2]
print(solution(45))