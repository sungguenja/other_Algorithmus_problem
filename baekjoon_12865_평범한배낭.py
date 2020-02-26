max_value = 0

def backpack(gram,value_list,now_gram=0,now_value=0):
    global max_value
    if gram<now_gram:
        return
    
    if max_value<now_value:
        max_value = now_value
    
    for i in range(len(value_list)):
        if visit[i] == 0:
            visit[i] = 1
            backpack(gram,value_list,now_gram+value_list[i][0],now_value+value_list[i][1])
            visit[i] = 0

N,K=map(int,input().split())
gram_value = [0]*N
for i in range(N):
    G,V = map(int,input().split())
    gram_value[i] = [G,V]
visit = [0]*N
backpack(K,gram_value)
print(max_value)