class node :
    def __init__(self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val

def ToQueueExpr(s) :
    q = [s]
    res = []
    while q != [] :
        u = q[0]
        del(q[0])
        res.append(u.val)
        if u.left != None :
            q.append(u.left)
        if u.right != None :
            q.append(u.right)
    res.reverse()
    return "".join(item for item in res)

def PostToNode(s) :
    qnode = []
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for l in range(len(s)) :
        if s[l] in upper :
            x = qnode[len(qnode) - 1]
            qnode.pop()
            y = qnode[len(qnode) - 1]
            qnode.pop()
            qnode.append(node(y, x, s[l]))
        else :
            qnode.append(node(None, None, s[l]))
    return qnode[0]

n = int(input())
for i in range(n) :
    s = input()
    print(ToQueueExpr(PostToNode(s)))