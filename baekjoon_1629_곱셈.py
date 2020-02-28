def big_num(num,start,end,div_num):
    if start==end:
        return num%div_num
    else:
        x=big_num((num%div_num)**2,start,(start+end)//2,div_num)
        y=big_num((num%div_num)**2,(start+end)//2+1,end,div_num)
        return final_num(x,y,div_num)

def final_num(forward,behind,div_num):
    return forward%div_num


A,B,C=map(int,input().split())
print(big_num(A%C,1,B,C))
