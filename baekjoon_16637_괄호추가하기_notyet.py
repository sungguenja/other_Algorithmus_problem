# def bracket_exp(N,exp,num=[]):
#     if visit == [1]*(N//2):
#         root.append(num)
#         return

#     for i in range(N//2):
#         if visit[i] == 0:
#             visit[i] = 1
#             bracket_exp(N,exp,num+[i])
#             visit[i] = 0

# 생각 잘못했다 시부장

# N=int(input())
# exp = list(input())
# copy_exp = exp[:]
# visit = [0]*(N//2)
# root=[]
# bracket_exp(N,exp)
# su = -10*(N//2+1)
# for i in range(len(root)):
#     exp = copy_exp[:]
#     for j in range(N//2):
#         if exp[2*(root[i][j])+1] == '+':
#             exp[2*(root[i][j]):2*(root[i][j])+3] = [int(exp[2*(root[i][j])])+int(exp[2*(root[i][j])+2])]*3
#         elif exp[2*(root[i][j])+1] == '-':
#             exp[2*(root[i][j]):2*(root[i][j])+3] = [int(exp[2*(root[i][j])])-int(exp[2*(root[i][j])+2])]*3
#         elif exp[2*(root[i][j])+1] == '*':
#             exp[2*(root[i][j]):2*(root[i][j])+3] = [int(exp[2*(root[i][j])])*int(exp[2*(root[i][j])+2])]*3
#     if su<exp[2*(root[i][j])+1]:
#         su = exp[2*(root[i][j])+1]
# print(su)