from collections import deque
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
word_board = [tuple(input()) for i in range(N)]
word_board = tuple(word_board)
find_word = tuple(input())

def solution(start_i,start_j,word,length,N,M,K):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    answer = 0
    Que = deque()
    Que.append((start_i,start_j,0))
    while Que:
        i,j,cost = Que.popleft()
        if cost == length-1:
            answer += 1
            continue
        for can_go in range(K):
            for k in range(4):
                ni = i + (can_go+1)*di[k]
                nj = j + (can_go+1)*dj[k]
                if 0<=ni<N and 0<=nj<M and word_board[ni][nj] == word[cost+1]:
                    Que.append((ni,nj,cost+1))
    return answer

result = 0
for i in range(N):
    for j in range(M):
        if word_board[i][j] == find_word[0]:
            result += solution(i,j,find_word,len(find_word),N,M,K)
reversed_word = tuple(reversed(find_word))
if reversed_word == find_word:
    result = result // 2
print(result)