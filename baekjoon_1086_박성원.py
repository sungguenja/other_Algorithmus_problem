from sys import stdin
from itertools import permutations
input = stdin.readline

numerator   = 0
denominator = 0
def makePermanent(array,length,checker):
    global numerator,denominator
    permutations_list = permutations(array,length)
    for permutation in permutations_list:
        denominator += 1
        if int(''.join(permutation))%checker == 0:
            numerator += 1

def getGCD(x,y):
    while y:
        x,y=y,x%y
    return x

N = int(input().strip())
arr = [str(input().strip()) for i in range(N)]
K = int(input().strip())

makePermanent(arr,N,K)
if numerator == 0:
    denominator = 1
elif numerator == denominator:
    numerator = 1
    denominator = 1
else:
    gcd = getGCD(denominator,numerator)
    numerator = numerator // gcd
    denominator = denominator // gcd

print("{0}/{1}".format(numerator,denominator))