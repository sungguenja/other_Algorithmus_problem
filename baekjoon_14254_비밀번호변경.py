before_password = list(input())
K = int(input())
visit = [False]*len(before_password)
pair = [None]*len(before_password)
left = ''.join(before_password[:K])
right = ''.join(before_password[len(before_password)-K:])
answer = 0
if len(before_password) - K < K:
    if left != right:
        for i in range(K):
            if before_password[i] != '?' and before_password[-K+i] != '?' and before_password[i] != before_password[-K+i]:
                before_password[-K+i] = '?'
        print(before_password)
        nl = before_password[:K]
        nr = before_password[-K:]
        print(nl,nr)
else:
    for i in range(K):
        if left[i] != right[i]:
            answer += 1

print(answer)
print(left,right)