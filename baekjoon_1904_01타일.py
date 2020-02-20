#피보나치네....
memo = [0,1,2]
def floor(N):
    global memo
    if N>=3 and len(memo)<N+1:
        memo.append(floor(N-1)+floor(N-2))
    return memo[N]
print(floor(int(input())))