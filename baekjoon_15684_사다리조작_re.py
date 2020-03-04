def game(N,M):
    global c_bridge

    for j in range(N):
        ni=0
        nj=j
        goal = 5
        while ni != M:
            if c_bridge[ni][nj] == 1 and goal != 0:
                while c_bridge[ni][nj] == 1:
                    nj+=1
                goal=1
            if nj-1>=0 and c_bridge[ni][nj-1] == 1 and goal != 1:
                while nj-1>=0 and c_bridge[ni][nj-1]==1:
                    nj-=1
                goal=0
            if c_bridge[ni][nj]==0 or goal!=2:
                ni+=1
                goal=2
        if nj!=j:
            break
    else:
        return True
    return False 