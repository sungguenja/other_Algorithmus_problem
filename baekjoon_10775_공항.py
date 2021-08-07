from sys import stdin
input = stdin.readline

G = int(input())
arr = [True]*(G+1)
P = int(input())
for i in range(P):
    small_g = int(input())
    for k in range(small_g,0,-1):
        if arr[k]:
            arr[k] = False
            break
    else:
        print(i)
        break
else:
    print(P)