import sys
sys.setrecursionlimit(10000)
def solution(user_id,banned_id):
    asdf=[0]
    visit = [0]*len(user_id)
    case = []
    def find(j=0):
        if j == len(banned_id):
            if visit not in case:
                X=visit[:]
                case.append(X)
                asdf[0] += 1
            return
        
        for i in range(len(user_id)):
            if len(banned_id[j]) == len(user_id[i]) and visit[i] == 0:
                for k in range(len(banned_id[j])):
                    if banned_id[j][k] == '*':
                        continue
                    elif banned_id[j][k] != user_id[i][k]:
                        break
                else:
                    visit[i] = 1
                    find(j+1)
                    visit[i] = 0
    find()
    return asdf[0]