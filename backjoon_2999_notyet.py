ur_word = list(input())
R = 1
R_save = 1
C = len(ur_word)
C_save = 0
while R<=C:
    if R*C == len(ur_word) and R_save<R:
        R_save = R
        C_save = C
    R += 1
    C = len(ur_word)//R
num = 0
password = [[0]*(R_save) for _ in range(C_save)]
for i in range(C_save):
    for j in range(R_save):
        password[i][j] = ur_word[num]
        num += 1

for k in password:
    print(k)