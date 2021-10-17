L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))

delta_x_1 = L1[0] - L1[2]
delta_y_1 = L1[1] - L1[3]
delta_x_2 = L2[0] - L2[2]
delta_y_2 = L2[1] - L2[3]

a = delta_x_1
b = -delta_y_1
c = delta_x_2
d = -delta_y_2

start_x_1 = min(L1[0],L1[2])
end_x_1 = max(L1[0],L1[2])
start_x_2 = min(L2[0],L2[2])
end_x_2 = max(L2[0],L2[2])
start_y_1 = min(L1[1],L1[3])
end_y_1 = max(L1[1],L1[3])
start_y_2 = min(L2[1],L2[3])
end_y_2 = max(L2[1],L2[3])

if a*d - b*c == 0:
    if delta_x_1 != 0 and delta_x_2 != 0:
        first_y_slash = L1[1] - (delta_y_1/delta_x_1)*L1[0]
        second_y_slash = L2[1] - (delta_y_2/delta_x_2)*L2[0]
        if first_y_slash == second_y_slash:
            if start_x_1<=start_x_2<=end_x_1 or start_x_2<=start_x_1<=end_x_2 or start_x_1<=end_x_2<=end_x_1 or start_x_2<=end_x_1<=end_x_2:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        if delta_x_1 == 0 and delta_x_2 == 0:
            if L1[1] != L2[1]:
                print(0)
            else:
                if start_y_1<=start_y_2<=end_y_1 or start_y_2<=start_y_1<=end_y_2 or start_y_1<=end_y_2<=end_y_1 or start_y_2<=end_y_1<=end_y_2:
                    print(1)
                else:
                    print(0)
        else:
            y = float((1/(a*d-b*c))*(d*(a*L1[1]+b*L1[0])+(-b)*(c*L2[1]+d*L2[0])))
            x = float((1/(a*d-b*c))*((-c)*(a*L1[1]+b*L1[0])+a*(c*L2[1]+d*L2[0])))
            
            
            if start_x_1<=x<=end_x_1 and start_x_2<=x<=end_x_2 and start_y_1<=y<=end_y_1 and start_y_2<=y<=end_y_2:
                print(1)
            else:
                print(0)
else:
    y = float((1/(a*d-b*c))*(d*(a*L1[1]+b*L1[0])+(-b)*(c*L2[1]+d*L2[0])))
    x = float((1/(a*d-b*c))*((-c)*(a*L1[1]+b*L1[0])+a*(c*L2[1]+d*L2[0])))
    
    
    if start_x_1<=x<=end_x_1 and start_x_2<=x<=end_x_2 and start_y_1<=y<=end_y_1 and start_y_2<=y<=end_y_2:
        print(1)
    else:
        print(0)