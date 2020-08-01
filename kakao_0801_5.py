def closestStraightCity(c, x, y, q):
    # Write your code here
    case = [0]*len(c)
    for i in range(len(c)-1):
        shortest_distance = 10**18
        shortest_city = ''
        for j in range(i+1,len(c)):
            if x[j] == x[i]:
                now_distance = abs(y[j]-y[i])
                if shortest_distance>now_distance:
                    shortest_city = c[j]
                    shortest_distance = now_distance
                elif shortest_distance == now_distance:
                    if len(shortest_city)>len(c[j]):
                        shortest_city = c[j]
                    elif len(shortest_city) == len(c[j]):
                        shortest_city = min(shortest_city,c[j])
            if y[j] == y[i]:
                now_distance = abs(x[j]-x[i])
                if shortest_distance>now_distance:
                    shortest_city = c[j]
                    shortest_distance = now_distance
                elif shortest_distance == now_distance:
                    if len(shortest_city)>len(c[j]):
                        shortest_city = c[j]
                    elif len(shortest_city) == len(c[j]):
                        shortest_city = min(shortest_city,c[j])
        if shortest_city == '':
            case[q.index(c[i])] = 'NONE'
        else:
            case[q.index(c[i])] = shortest_city
    
    return case

print(min('abd','abdd','cc'))