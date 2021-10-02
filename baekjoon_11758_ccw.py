import sys
import math
from decimal import Decimal
INF = sys.maxsize

first  = list(map(int,input().split()))
second = list(map(int,input().split()))
third  = list(map(int,input().split()))

def makeInclination(amount_of_change_x,amount_of_change_y):
    if amount_of_change_x == 0:
        return INF
    return Decimal(amount_of_change_y / amount_of_change_x)

weight_point = [(first[0]+second[0]+third[0])//3,(first[1]+second[1]+third[1])//3]
first = [first[0]-weight_point[0],first[1]-weight_point[1]]
second = [second[0]-weight_point[0],second[1]-weight_point[1]]
third = [third[0]-weight_point[0],third[1]-weight_point[1]]

first_amount_of_change_x = second[0] - first[0]
first_amount_of_change_y = second[1] - first[1]
second_amount_of_change_x = third[0] - second[0]
second_amount_of_change_y = third[1] - second[1]
first_amount_of_change_x_direction = first_amount_of_change_x >= 0
first_amount_of_change_y_direction = first_amount_of_change_y >= 0
second_amount_of_change_x_direction = second_amount_of_change_x >= 0
second_amount_of_change_y_direction = second_amount_of_change_y >= 0

first_inclination = makeInclination(first_amount_of_change_x,first_amount_of_change_y)
second_inclination = makeInclination(second_amount_of_change_x,second_amount_of_change_y)

if first_inclination == second_inclination:
    if (first_amount_of_change_x_direction == second_amount_of_change_x_direction and first_amount_of_change_y_direction == second_amount_of_change_y_direction):
        print(0)
    else:
        # 직선처리가 어떻게 되야 하지?
        pass
else:
    first_point_degree = math.atan2(first[1],first[0])
    second_point_degree = math.atan2(second[1],second[0])
    third_point_degree = math.atan2(third[1],third[0])

    if first_point_degree <= second_point_degree <= third_point_degree:
        print(1)
    else:
        print(-1)