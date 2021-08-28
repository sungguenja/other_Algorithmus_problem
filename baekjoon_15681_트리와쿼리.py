import sys
from collections import deque
sys.setrecursionlimit(200000)
input = sys.stdin.readline

class Node:
    def __init__(self,num):
        self.number = num
        self.parent = None
        self.child_list = []
        self.child_cnt = 0
    
    def addChild(self,child):
        self.child_list.append(child)
        child.parent = self
        self.child_cnt += 1

    def findTreeCNT(self):
        answer = self.child_cnt
        for child in self.child_list:
            if answer_list[child.number] != None:
                answer += answer_list[child.number]
            elif child.child_cnt >= 1:
                answer += child.findTreeCNT()
        answer_list[self.number] = answer
        if self.parent != None and self.parent.child_cnt == 1:
            answer_list[self.parent.number] = answer + 1
        return answer

def makeNodeList(route,start):
    Que = deque()
    Que.append(start)
    visit = [False]*(len(route))
    visit[start] = True
    node_list = [Node(i) for i in range(N+1)]
    while Que:
        now = Que.popleft()
        for goal in route[now]:
            if not visit[goal]:
                visit[goal] = True
                node_list[now].addChild(node_list[goal])
                Que.append(goal)
    return node_list

N,R,Q = map(int,input().split())
route = [[] for i in range(N+1)]

for _ in range(N-1):
    first_point, second_point = map(int,input().split())
    route[first_point].append(second_point)
    route[second_point].append(first_point)

node_list = makeNodeList(route,R)
answer_list = [None]*(N+1)

for _ in range(Q):
    node = int(input())
    if answer_list[node] == None:
        print(node_list[node].findTreeCNT() + 1)
    else:
        print(answer_list[node] + 1)