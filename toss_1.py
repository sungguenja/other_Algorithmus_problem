# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(map(int,input().split()))
case = [8,5,2,4,3,7,6,1,0,9]
cnt = 0
answer = [0]*len(user_input)
for i in case:
    for j in user_input:
        if i==j:
            answer[cnt] = i
            cnt+=1
print(answer)