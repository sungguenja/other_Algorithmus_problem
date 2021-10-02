first  = list(map(int,input().split()))
second = list(map(int,input().split()))
third  = list(map(int,input().split()))

first_vector = [second[0]-first[0],second[1]-first[1],0]
second_vector = [third[0]-second[0],third[1]-second[1],0]
cross_product = first_vector[0]*second_vector[1]-first_vector[1]*second_vector[0]

if cross_product > 0:
    print(1)
elif cross_product < 0:
    print(-1)
else:
    print(0)