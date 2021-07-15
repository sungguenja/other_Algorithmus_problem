import sys
sys.setrecursionlimit(99999)
def makeTrie(now_trie,start,left_limit,right_limit):
    if now_trie == 1:
        print(post_order[start],end=" ")
        return
    elif now_trie == 0:
        return
    head = post_order[start]
    head_position = in_order.index(head)
    print(head,end=" ")
    if head_position - left_limit >= 1 and head_position-left_limit-1 != 0:
        makeTrie(head_position-left_limit-1,start-(right_limit-head_position-1)-1,left_limit,head_position)
    if right_limit - head_position >= 1 and right_limit-head_position-1 != 0:
        makeTrie(right_limit-head_position-1,start-1,head_position,right_limit)
N = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
makeTrie(N,N-1,-1,N)