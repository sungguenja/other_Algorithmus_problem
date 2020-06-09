from math import ceil
def solution(n, stations, w):
    answer = 0
    if len(stations) != 1:
        for i in range(len(stations)):
            if i==0:
                if stations[i]-w>1:
                    answer += ceil((stations[i]-w-1)/(2*w+1))
            elif i==len(stations)-1:
                if stations[i]-w>stations[i-1]+w:
                    answer += ceil((stations[i]-w-stations[i-1]-w-1)/(2*w+1))
                if stations[i]+w<n:
                    answer += ceil((n-(stations[i]+w))/(2*w+1))
            else:
                if stations[i]-w>stations[i-1]+w:
                    answer += ceil((stations[i]-w-(stations[i-1]+w)-1)/(2*w+1))
    else:
        if stations[0]-w>1:
            answer += ceil((stations[0]-w)/(2*w+1))
        if stations[0]+w<n:
            answer += ceil((n-(stations[0]+w))/(2*w+1))
    return answer