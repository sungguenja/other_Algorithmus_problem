import sys
sys.setrecursionlimit(9999)
answer = [[],[]]
trigger = False
class Node:
    def __init__(self,number,x,y):
        self.number = number
        self.parent = None
        self.position = [x,y]
        self.left = None
        self.right = None
    
    def preorder(self):
        global answer
        answer[0].append(self.number)
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
    
    def postorder(self):
        global answer
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        answer[1].append(self.number)
    
    def leftChecker(self,child_x):
        global trigger
        if self.position[0] < child_x:
            return False
        else:
            if self.parent == None:
                trigger = True
                return True
            else:
                if self.parent.left == self:
                    self.parent.leftChecker(child_x)
                elif self.parent.right == self:
                    self.parent.rightChecker(child_x)
                return trigger
    
    def rightChecker(self,child_x):
        global trigger
        if self.position[0] > child_x:
            return False
        else:
            if self.parent == None:
                trigger = True
                return True
            else:
                if self.parent.left == self:
                    self.parent.leftChecker(child_x)
                elif self.parent.right == self:
                    self.parent.rightChecker(child_x)
                return trigger

def solution(nodeinfo):
    global answer,trigger
    y_position = {}
    node_list = []
    root = -1
    for i in range(len(nodeinfo)):
        x,y = nodeinfo[i]
        node = Node(i+1,x,y)
        if y > root:
            root = y

        if y_position.get(y) == None:
            y_position[y] = [node]
        else:
            y_position[y].append(node)

        node_list.append(node)
        
    node_list.sort(key = lambda x : (-x.position[1],x.position[0]))
    for y in y_position.keys():
        y_position[y].sort(key = lambda x : (x.position[0],x.number))

    now = root - 1
    before_root = root
    while root > -1:
        if now not in y_position.keys() and now > -1:
            now -= 1
            continue
        if now <= -1:
            break
        for parent_node in y_position[root]:
            for child_node in y_position[now]:
                trigger = False
                if child_node.position[0] > parent_node.position[0]:
                    if child_node.parent == None:
                        if parent_node.rightChecker(child_node.position[0]):
                            parent_node.right = child_node
                            child_node.parent = parent_node
                            break
                elif child_node.position[0] < parent_node.position[0]:
                    if child_node.parent == None:
                        if parent_node.leftChecker(child_node.position[0]):
                            parent_node.left = child_node
                            child_node.parent = parent_node
        root -= 1
        while root > -1 and root not in y_position.keys():
            root -= 1
        now = root - 1

    node_list[0].preorder()
    node_list[0].postorder()
    return answer
