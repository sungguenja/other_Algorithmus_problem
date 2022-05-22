answer = 0
def makeT(inner_S,inner_T):
    global answer
    if answer == 1:
        return
    
    A_S = inner_S + 'A'
    B_S = (inner_S + 'B')[::-1]
    
    if len(A_S) == len(inner_T):
        if A_S == inner_T:
            answer = 1
        elif B_S == inner_T:
            answer = 1
        return
    
    check_A = True
    check_reverse_A = True
    check_B = True
    check_reverse_B = True
    for i in range(len(A_S)):
        if A_S[i] != inner_T[i]:
            check_A = False
        if A_S[-i] != inner_T[-i]:
            check_reverse_A = False
        if B_S[i] != inner_T[i]:
            check_B = False
        if B_S[-i] != inner_T[-i]:
            check_reverse_B
        if not check_A and not check_reverse_A and not check_B and not check_reverse_B:
            break
    
    if answer == 0 and (check_A or check_reverse_A):
        makeT(A_S,inner_T)
    if answer == 0 and (check_B or check_reverse_B):
        makeT(B_S,inner_T)
S = str(input())
T = str(input())
if len(S) <= len(T):
    makeT(S,T)
print(answer)