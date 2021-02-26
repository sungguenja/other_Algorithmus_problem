N = int(input())
arr = list(map(int,input().split()))
arr.sort()
left = 0
right = N-1
num1 = 99999999999999
num2 = 99999999999999
check = num1+num2

while left<right:
    now = arr[left] + arr[right]
    if abs(now)<=abs(check):
        num1 = arr[left]
        num2 = arr[right]
        check = now
    
    if now>=0:
        right -= 1
    else:
        left += 1

if num1>num2:
    num1,num2=num2,num1

print(num1,num2)