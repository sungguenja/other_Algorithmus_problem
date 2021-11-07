class AntHouse:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.parent = None
        self.child = []
    
    def printNode(self):
        print('{0}{1}'.format('-'*(self.number*2),self.name))
        for child in self.child:
            child.printNode()
    
    def addChild(self,arr):
        if len(arr) == 0:
            return

        for child in self.child:
            if child.name == arr[0]:
                child.addChild(arr[1:])
                break
        else:
            self.child.append(AntHouse(arr[0],self.number+1))
            self.child[-1].addChild(arr[1:])
    
    def sortNode(self):
        self.child.sort(key=lambda x: x.name)
        for child in self.child:
            child.sortNode()
    

N = int(input())
node_list = []
for _ in range(N):
    arr = list(input().split())
    for node in node_list:
        if node.name == arr[1]:
            node.addChild(arr[2:])
            break
    else:
        node_list.append(AntHouse(arr[1],0))
        node_list[-1].addChild(arr[2:])

node_list.sort(key=lambda x: x.name)

for head_node in node_list:
    head_node.sortNode()

for head_node in node_list:
    head_node.printNode()