tetromino = [[[0,1],[0,2],[0,3]],
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

N,M = map(int,input().split())
game = []
for i in range(N):
    game.append(list(map(int,input().split())))

answer = 0
for i in range(N):
    for j in range(M):
        for tetro in tetromino:
            score = game[i][j]
            for tet in tetro:
                ni = i + tet[0]
                nj = j + tet[1]
                if 0<=ni<N and 0<=nj<M:
                    score += game[ni][nj]
            if answer<score:
                answer = score

print(answer)