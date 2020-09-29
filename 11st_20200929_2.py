# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    N = len(S)
    M = len(S[0])
    for i in range(M):
        spell = [word[i] for word in S]
        spell_set = set(spell)
        if N != len(spell_set):
            for word in spell_set:
                answer = []
                cnt = 0
                for k in range(N):
                    if spell[k] == word:
                        answer.append(k)
                        cnt+=1
                        if cnt>=2:
                            answer.append(i)
                            return answer
    return []

print(solution(['zzzz','ferz','zdsr','fgtd']))
print(solution(['abc', 'bca', 'dbe']))
print(solution(['gr', 'sd', 'rg']))