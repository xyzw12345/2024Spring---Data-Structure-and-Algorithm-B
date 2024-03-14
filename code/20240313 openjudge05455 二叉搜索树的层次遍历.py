class node :
    def __init__(self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val

def insert(x, s) :
    if s == None :
        return node(None, None, x)
    if x > s.val :
        return node(s.left, insert(x, s.right), s.val)
    if x < s.val :
        return node(insert(x, s.left), s.right, s.val)
    return s

def ToQString(s) :
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
    return " ".join(str(item) for item in res)

s = None
s1 = list(map(int, input().split()))
for i in s1 :
    s = insert(i, s)
print(ToQString(s))