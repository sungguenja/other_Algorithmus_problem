from sys import stdin
input = stdin.readline

N = int(input())
start_point = list(map(int,input().split()))
trigger = True
answer = 0

for i in range(N-2):
    if trigger:
        trigger = False
        first_vector = list(map(int,input().split()))
        second_vector = list(map(int,input().split()))
        first_vector = [first_vector[0]-start_point[0],first_vector[1]-start_point[1]]
        second_vector = [second_vector[0]-start_point[0],second_vector[1]-start_point[1]]

        answer += abs((first_vector[0]*first_vector[1] + second_vector[0]*second_vector[1])/2)
        first_vector = second_vector[:]
        continue

    second_vector = list(map(int,input().split()))
    second_vector = [second_vector[0]-start_point[0],second_vector[1]-start_point[1]]
    answer += abs((first_vector[0]*first_vector[1] + second_vector[0]*second_vector[1])/2)
    first_vector = second_vector[:]

print(round(answer,1))