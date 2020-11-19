class Node:
    def __init__(self,val,leaf=False):
        self.val = val
        self.leaf = leaf
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur = self.head

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
        
        cur.leaf = True
    
    def search(self,prefix,num):
        ret = 0
        cur = self.head

        for c in prefix:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return 0
        
        node_list = []
        for c in cur.child:
            node_list.append(cur.child[c])
        
        for i in range(num-1):
            temp = []
            for node in node_list:
                for c in node.child:
                    temp.append(node.child[c])
            node_list = temp
        
        for i in node_list:
            if i.leaf:
                ret += 1
        
        return ret

def solution(words, queries):
    answer = []

    trie = Trie()
    reverse_trie = Trie()

    for w in words:
        trie.insert(w)
        reverse_trie.insert(w[::-1])
    
    for query in queries:
        trigger = False
        if query[0] == '?' and query[-1] != '?':
            trigger = True
            query = query[::-1]
        
        pre = 0
        cnt = 0
        for idx,c in enumerate(query):
            if c=='?':
                pre = idx
                cnt = len(query)-idx
                break
        
        if trigger:
            answer.append(reverse_trie.search(query[:pre],cnt))
        else:
            answer.append(trie.search(query[:pre],cnt))
    
    return answer