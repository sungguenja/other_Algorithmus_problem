class Node:
    def __init__(self,number):
        self.number = number
        self.parent = None
        self.child = []
    
    def addChild(self,child):
        child.parent = self
        self.child.append(child)

for _ in range((int(input()))):
    N = int(input())
    node_list = [Node(i) for i in range(N+1)]
    visit = [False]*(N+1)
    for t in range(N-1):
        parent,child = map(int,input().split())
        node_list[parent].addChild(node_list[child])
    
    descendant_1, descendant_2 = map(int,input().split())
    visit[descendant_1] = True
    visit[descendant_2] = True
    while True:
        if descendant_1 != None:
            descendant_1 = node_list[descendant_1].parent
            if descendant_1 != None:
                descendant_1 = descendant_1.number
                if visit[descendant_1]:
                    print(descendant_1)
                    break
                else:
                    visit[descendant_1] = True
        if descendant_2 != None:
            descendant_2 = node_list[descendant_2].parent
            if descendant_2 != None:
                descendant_2 = descendant_2.number
                if visit[descendant_2]:
                    print(descendant_2)
                    break
                else:
                    visit[descendant_2] = True