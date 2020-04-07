case = 0
def find(N,r,c,start_i=0,start_j=0,end=False):
    global case
    if N>=2:
        if start_i<=r<start_i+2**(N-1) and start_j<=c<start_j+2**(N-1):
            find(N-1,r,c,start_i,start_j)
        elif start_i<=r<start_i+2**(N-1) and c>=start_j+2**(N-1):
            case+=2**(2*(N-1))
            find(N-1,r,c,start_i,start_j+2**(N-1))
        elif r>=start_i+2**(N-1) and start_j<=c<start_j+2**(N-1):
            case+=(2**(2*(N-1)))*2
            find(N-1,r,c,start_i+2**(N-1),start_j)
        elif r>=start_i+2**(N-1) and c>=start_j+2**(N-1):
            case+=(2**(2*(N-1)))*3
            find(N-1,r,c,start_i+2**(N-1),start_j+2**(N-1))
    elif N==1:
        if start_i<=r<start_i+2 and start_j<=c<start_j+2:
            for i in range(start_i,start_i+2):
                for j in range(start_j,start_j+2):
                    if i!=r or j!=c:
                        case+=1
                    else:
                        print(case)
                        return 1
        else:
            case+=4

N,r,c = map(int,input().split())
find(N,r,c)