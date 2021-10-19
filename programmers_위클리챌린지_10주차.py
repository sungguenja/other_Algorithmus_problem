import sys
INF = sys.maxsize

def makeCrossPoint(line):
    result = set()
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            A,B,E = line[i]
            C,D,F = line[j]
            if (A*D-B*C) != 0:
                X = (B*F-E*D)/(A*D-B*C)
                Y = (E*C-A*F)/(A*D-B*C)
                if int(X) == X and int(Y) == Y:
                    result.add((int(X),int(Y)))
    return result

def makeNewCrossSet(crossSet,minimum_x,minimum_y):
    result = set()
    for point in crossSet:
        x,y = point
        if minimum_x < 0:
            x += abs(minimum_x)
        else:
            x -= minimum_x
        if minimum_y < 0:
            y += abs(minimum_y)
        else:
            y -= minimum_y
        result.add((x,y))
    return result

def makeLengthAndCrossSet(crossSet):
    minimum_x = INF
    maximum_x = -INF
    minimum_y = INF
    maximum_y = -INF
    for point in crossSet:
        x,y = point
        if x < minimum_x:
            minimum_x = x
        if x > maximum_x:
            maximum_x = x
        if y < minimum_y:
            minimum_y = y
        if y > maximum_y:
            maximum_y = y
    return maximum_x-minimum_x+1,maximum_y-minimum_y+1,makeNewCrossSet(crossSet,minimum_x,minimum_y)
    
def solution(line):
    crossSet = makeCrossPoint(line)
    length_x,length_y,newCrossSet = makeLengthAndCrossSet(crossSet)
    answer = ['.'*length_x for _ in range(length_y)]
    for point in newCrossSet:
        j,i = point
        answer[i] = answer[i][:j] + '*' + answer[i][j+1:]
    return answer[::-1]