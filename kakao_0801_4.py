def prison(n, m, h, v):
    # Write your code here
    h.sort()
    v.sort()
    if len(h) != 1:
        maxmum_vertical = 1
        cnt = 2
        for i in range(1,len(h)):
            if h[i-1] + 1 == h[i]:
                cnt += 1
            else:
                if maxmum_vertical<cnt:
                    maxmum_vertical = cnt
                cnt = 2
        if maxmum_vertical<cnt:
            maxmum_vertical = cnt
    else:
        maxmum_vertical = 2
    
    if len(v)!=1:
        cnt = 2
        maxmum_horizon = 1
        for j in range(1,len(v)):
            if v[j-1] + 1 == v[j]:
                cnt += 1
            else:
                if maxmum_horizon<cnt:
                    maxmum_horizon = cnt
                cnt = 2
        if maxmum_horizon<cnt:
            maxmum_horizon = cnt
    else:
        maxmum_horizon = 2
    return maxmum_horizon*maxmum_vertical

print(prison(3,2,[1,2,3],[1,2]))