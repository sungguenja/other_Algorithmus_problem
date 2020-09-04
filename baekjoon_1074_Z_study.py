case = 0
def solution(N,r,c,start_i=0,start_j=0):
    global case
    if N>=2:
        next_i = start_i + 2**(N-1)
        next_j = start_j + 2**(N-1)
        if start_i <= r < next_i and start_j <= c < next_j:
            if solution(N-1,r,c,start_i,start_j):
                return True
            else:
                return False
        elif start_i <= r < next_i and c >= next_j:
            case += 2**(2*(N-1))
            if solution(N-1,r,c,start_i,next_j):
                return True
            else:
                return False
        elif r >= next_i and start_j <= c < next_j:
            case += 2*2**(2*(N-1))
            if solution(N-1,r,c,next_i,start_j):
                return True
            else:
                return False
        elif r >= next_i and c >= next_j:
            case += 3*2**(2*(N-1))
            if solution(N-1,r,c,next_i,next_j):
                return True
            else:
                return False
    elif N == 1:
        if start_i<=r<start_i+2 and start_j<=c<start_j+2:
            for i in range(start_i,start_i+2):
                for j in range(start_j,start_j+2):
                    if i==r and j==c:
                        print(case)
                        return True
                    else:
                        case += 1
            return False
        else:
            case += 4
            return False
N,r,c = map(int,input().split())
solution(N,r,c)