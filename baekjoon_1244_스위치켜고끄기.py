N = int(input())
switch = list(map(int,input().split()))
students_count = int(input())

def male_function(number):
    start_number = number - 1
    while start_number < N:
        if switch[start_number] == 1:
            switch[start_number] = 0
        else:
            switch[start_number] = 1
        start_number += number

def female_function(number):
    pivot = number - 1
    left = pivot
    right = pivot
    while left >= 0 and right < N and switch[left] == switch[right]:
        if switch[left] == 1:
            switch[left] = 0
            switch[right] = 0
        else:
            switch[left] = 1
            switch[right] = 1
        left -= 1
        right += 1

for student in range(students_count):
    gender,now_number = map(int,input().split())
    if gender == 1:
        male_function(now_number)
    else:
        female_function(now_number)
for i in range(0,N,20):
    print(" ".join(map(str,switch[i:i+20])))