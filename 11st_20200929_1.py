# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    answer = 0
    cnt = 0
    N = len(S)
    for i in range(N):
        if S[i] == 'a':
            cnt += 1
        else:
            cnt = 0
            if i == N-1:
                answer += 2
            elif i == N-2:
                if S[i+1] != 'a':
                    answer += 2
                else:
                    answer += 1
            elif i == 0:
                answer += 2
                if S[i+1] != 'a':
                    answer += 2
                else:
                    if S[i+2] != 'a':
                        answer += 1
            elif i == 1:
                if S[0] == 'a':
                    answer += 1
                if S[i+1] != 'a':
                    answer += 2
                else:
                    if S[i+2] != 'a':
                        answer += 1
            else:
                if S[i+1] != 'a':
                    answer += 2
                else:
                    if S[i+2] != 'a':
                        answer += 1
        if cnt>=3:
            answer = -1
            break
    return answer
print(solution('aabab'))
print(solution('dog'))
print(solution('aa'))
print(solution('baaaa'))