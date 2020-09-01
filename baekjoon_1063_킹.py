king,rock,N=input().split()
N = int(N)
king_where = [8-int(king[1]),ord(king[0])-ord('A')]
rock_where = [8-int(rock[1]),ord(rock[0])-ord('A')]
direction = {'R':[0,1],'L':[0,-1],'B':[1,0],'T':[-1,0],'RT':[-1,1],'LT':[-1,-1],'RB':[1,1],'LB':[1,-1]}
for i in range(N):
    command = str(input())
    i,j = king_where[0],king_where[1]
    ni = i + direction[command][0]
    nj = j + direction[command][1]
    if 0<=ni<8 and 0<=nj<8:
        if [ni,nj] == rock_where:
            k,l = rock_where[0],rock_where[1]
            nk = k + direction[command][0]
            nl = l + direction[command][1]
            if 0<=nk<8 and 0<=nl<8:
                king_where = [ni,nj]
                rock_where = [nk,nl]
            else:
                continue
        else:
            king_where = [ni,nj]
    else:
        continue
answer_king = chr(king_where[1]+ord('A'))+str(8-king_where[0])
answer_rock = chr(rock_where[1]+ord('A'))+str(8-rock_where[0])
print(answer_king)
print(answer_rock)