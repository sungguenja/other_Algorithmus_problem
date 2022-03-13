class Node:
    def __init__(self,number):
        self.number = number
        self.before = None
        self.after = None
    
    def pushAfterNode(self,afterNode):
        self.after = afterNode
        afterNode.pushBeforeNode(self)
    
    def pushBeforeNode(self,beforeNode):
        self.before = beforeNode
    
    def deleteSelf(self):
        beforeNode = self.before
        afterNode = self.after
        if beforeNode != None:
            beforeNode.after = afterNode
        if afterNode != None:
            afterNode.before = beforeNode

def solution(n, k, cmd):
    node_list = [Node(i) for i in range(n)]
    for i in range(len(node_list)):
        node = node_list[i]
        if node.number == n - 1:
            before_node = node_list[-2]
            node.pushBeforeNode(before_node)
            break
        after_node = node_list[i+1]
        node.pushAfterNode(after_node)
    now = node_list[k]
    deleted_stack = []
    for cmd_string in cmd:
        cmd_string_list = list(cmd_string.split(" "))
        if len(cmd_string_list) == 1:
            if cmd_string_list[0] == 'C':
                now_after = now.after
                now_before = now.before
                deleted_stack.append(now.number)
                now.deleteSelf()
                if now_after != None:
                    now = now_after
                else:
                    now = now_before
            else:
                start = now
                relive_node = node_list[deleted_stack.pop()]
                if start.number < relive_node.number:
                    after_node = start.after
                    while after_node != None and after_node.number < relive_node.number:
                        start = after_node
                        after_node = after_node.after
                    if after_node != None:
                        after_node.before = relive_node
                    relive_node.after = after_node
                    relive_node.before = start
                    start.after = relive_node
                else:
                    after_node = start.after
                    while before_node != None and before_node.number > relive_node.number:
                        start = before_node
                        before_node = before_node.before
                    if before_node != None:
                        before_node.after = relive_node
                    relive_node.before = before_node
                    relive_node.after = start
                    start.before = relive_node
        else:
            cnt = int(cmd_string_list[1])
            if cmd_string_list[0] == 'D':
                for _ in range(cnt):
                    if now == None:
                        break
                    now = now.after
            else:
                for _ in range(cnt):
                    if now == None:
                        break
                    now = now.before
    answer_list = ['X']*n
    start = now
    while start != None:
        answer_list[start.number] = 'O'
        start = start.after
    start = now
    while start != None:
        answer_list[start.number] = 'O'
        start = start.before
    return ''.join(answer_list)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))