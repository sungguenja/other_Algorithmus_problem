tetro = [[[0,1],[0,2],[0,3]],
[[1,0],[2,0],[3,0]],
[[0,1],[1,0],[1,1]],
[[1,0],[2,0],[2,1]],
[[0,1],[0,2],[1,0]],
[[0,1],[1,1],[2,1]],
[[0,1],[0,2],[-1,2]],
[[1,0],[2,0],[2,-1]],
[[0,1],[0,2],[1,2]],
[[0,1],[1,0],[2,0]],
[[-1,0],[0,1],[0,2]],
[[0,1],[-1,1],[1,0]],
[[0,-1],[1,0],[1,1]],
[[0,-1],[-1,-1],[1,0]],
[[0,1],[1,0],[1,-1]],
[[0,-1],[0,1],[1,0]],
[[0,-1],[-1,0],[1,0]],
[[0,-1],[-1,0],[0,1]],
[[-1,0],[0,1],[1,0]]]

N,M=map(int,input().split())
tetis=[list(map(int,input().split())) for _ in range(N)]
max_tetro = 0
for i in range(N):
    for j in range(M):
        for tet in tetro:
            sum_tetro = tetis[i][j]
            for tet_c in tet:
                ni=i+tet_c[0]
                nj=j+tet_c[1]
                if 0<=ni<N and 0<=nj<M:
                    sum_tetro += tetis[ni][nj]
            if max_tetro<sum_tetro:
                max_tetro=sum_tetro
print(max_tetro)