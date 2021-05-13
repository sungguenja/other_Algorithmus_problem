memory = []
class Node:
    def __init__(self,number,value):
        self.number = number
        self.value = value
        self.parent = None
        self.childs = []

    def addChild(self,child):
        self.childs.append(child)
    
    def addParent(self,parent):
        self.parent = parent

    def addChildsValue(self):
        if memory[self.number] == 'not':
            now_sum = 0
            now_sum += self.value
            for child in self.childs:
                now_sum += child.addChildsValue()
            memory[self.number] = now_sum
            return now_sum
        else:
            return memory[self.number]

    def changeValue(self,value):
        if self.parent == None:
            self.value = value
        else:
            self.value = self.parent.value
            self.parent.changeValue(value)


def solution(values, edges, queries):
    global memory
    N = len(values)
    node_list = [0]
    memory = ['not']*(N+1)
    answer = []
    for i in range(len(values)):
        node_list.append(Node(i+1,values[i]))
    for family in edges:
        node_list[family[0]].addChild(node_list[family[1]])
        node_list[family[1]].addParent(node_list[family[0]])
    
    for query in queries:
        if query[1] == -1:
            if memory[node_list[query[0]].number] == 'not':
                node_list[query[0]].addChildsValue()
            answer.append(memory[node_list[query[0]].number])
        else:
            node_list[query[0]].changeValue(query[1])
            memory = ["not"]*(N+1)
    return answer