from collections import deque
answer = 0
def solution(one,two,three,checker):
    global answer
    visit = set()
    Que = deque()
    Que.append((one,two,three))
    while Que:
        i,j,k = Que.popleft()
        if i == j and j == k:
            answer = 1
            return
        i,j,k = sorted([i,j,k])
        k_minus_tuple = tuple(sorted([i*2,j,k-i]))
        j_minus_tuple = tuple(sorted([i*2,j-i,k]))
        if k_minus_tuple not in visit:
            visit.add(k_minus_tuple)
            Que.append(k_minus_tuple)
        if j_minus_tuple not in visit:
            visit.add(j_minus_tuple)
            Que.append(j_minus_tuple)
        

first,second,third = map(int,input().split())
first,second,third = sorted([first,second,third])
avg = (first+second+third)//3
if (first+second+third) % 3 == 0:
    solution(first,second,third,avg)
print(answer)