from collections import deque

class BinTreeNode :
    def __init__ (self, val, left = None, right = None) :
        self.left = left
        self.right = right
        self.val = val
    def toGenTree (self) :
        #print("togentree", self.Traversal("pre"), "building:", self.val)
        c = self.val 
        cur = self.left
        res = []
        while cur != None and cur.val != "$":
            res.append(cur.toGenTree())
            cur = cur.right
        #print(self.val, "Done")
        return GenTreeNode(c, res)
    def Traversal (self, mode) :
        u = "" if self.left == None else self.left.Traversal(mode)
        v = "" if self.right == None else self.right.Traversal(mode)
        if mode == "pre" :
            return self.val + " " + u + " " + v
        if mode == "mid" :
            return u + " " + self.val + " " + v
        if mode == "post" :
            return u + " " + v + " " + self.val
def _getnode (s) :
    if s[0][1] == "1" :
        return BinTreeNode(s[0][0]), 1
    else :
        c = s[0][0]
        u, lu = _getnode(s[1:])
        v, lv = _getnode(s[(lu + 1):])
        return BinTreeNode(c, u, v), lu + lv + 1
def getnode (s) :
    return _getnode(s)[0]    
class BinTree :
    def __init__ (self, s) :
        self.root = getnode(s)
    def Traversal (self, mode) :
        return self.root.Traversal(mode)
    def toGenTree (self) :
        return self.root.toGenTree()
class GenTreeNode :
    def __init__ (self, val, children = []) :
        self.children = children
        self.val = val
class GenTree :
    def __init__ (self, bintree) :
        self.root = bintree.toGenTree()
    def _mirror (self, pos) :
        pos.children.reverse()
        for child in pos.children :
            self._mirror(child)
    def mirror (self) :
        self._mirror(self.root)
    def level_traversal(self) :
        q = deque()
        q.append(self.root)
        res = []
        while len(q) > 0 :
            res.append(q[0].val)
            q.extend(q[0].children)
            q.popleft()
        return " ".join(item for item in res)

_ = int(input())
B = BinTree(input().split())
#print(B.Traversal("pre"))
#print(B.Traversal("mid"))
G = GenTree(B)
G.mirror()
print(G.level_traversal())