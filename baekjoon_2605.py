N=int(input())
number = list(map(int, input().split()))
line = []
for i in range(N):
    line.insert(number[i], i+1)
print(' '.join(map(str, line[-1::-1])))