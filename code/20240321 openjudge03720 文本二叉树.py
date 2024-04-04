
class node :
    def __init__ (self, left, right, val) :
        self.left = left
        self.right = right 
        self.val = val
    def traversal(self, mode) :
        s1 = ""
        s2 = ""
        if self.left != None :
            s1 = self.left.traversal(mode)
        if self.right != None :
            s2 = self.right.traversal(mode)
        if mode == "pre" :
            return self.val + s1 + s2
        if mode == "in" :
            return s1 + self.val + s2
        if mode == "post" :
            return s1 + s2 + self.val

def build(h) :
    if h == [] or h[0] == "":
        return None
    val = h[0][0]
    #print(val)
    #return node(None, None, val)
    if val == "*":
        return None
    if len(h) == 1 :
        return node(None, None, val)
    y = 2
    while y <= len(h) - 1 and len(h[y]) > 2 :
        y += 1
    #return node(None, None, val)
    if y == len(h) :
        return node(build(list(h[i][1 : len(h[i])] for i in range(1, y))), None, val)
    #print(h, list(h[i][1 : len(h[i])] for i in range(1, y)), list(h[i][1 : len(h[i])] for i in range(y, len(h))))
    return node(build(list(h[i][1 : len(h[i])] for i in range(1, y))), build(list(h[i][1 : len(h[i])] for i in range(y, len(h)))), val)    


CaseNum = int(input())
for Case in range(CaseNum) :
    h = []
    while True :
        s = input()
        if s == "0" :
            break
        h.append(s)
    #print(h)
    tree = build(h)
    print(tree.traversal("pre"))
    print(tree.traversal("post"))
    print(tree.traversal("in"))
    print("")
