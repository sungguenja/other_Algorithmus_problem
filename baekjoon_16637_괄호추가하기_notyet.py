from itertools import combinations
import copy

N=int(input())
exp = list(input())
new_exp = []
for i in range(0,N-1,2):
    new_exp.append(exp[i:i+3])

# 초기값 잡기
if new_exp[0][1] == '+':
    su = int(new_exp[0][0])+int(new_exp[0][2])
elif new_exp[0][1] == '-':
    su = int(new_exp[0][0])-int(new_exp[0][2])
elif new_exp[0][1] == '*':
    su = int(new_exp[0][0])*int(new_exp[0][2])
# 초기값 잡기 마무리
for i in range(1,N//2):
    if new_exp[i][1] == '+':
        su += int(new_exp[i][2])
    elif new_exp[i][1] == '-':
        su -= int(new_exp[i][2])
    elif new_exp[i][1] == '*':
        su *= int(new_exp[i][2])
print(su)

