class node :
    def __init__ (self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val

def getIndex(c, s) :
    for i in range(len(s)) :
        if c == s[i] :
            return i
    return -1

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
    return "".join(item for item in res)

def BuildTree_post_in(sp, si) :
    if sp == "" :
        return None
    l = getIndex(sp[len(sp) - 1], si)
#    print(sp, si, l, sep = " ")
    return node(BuildTree_post_in(sp[0 : l], si[0 : l]), BuildTree_post_in(sp[l : len(sp) - 1], si[l + 1 : len(si)]), sp[len(sp) - 1])

n = int(input())
for i in range(n) :
    s1 = input()
    s2 = input()
    print(ToQString(BuildTree_post_in(s2, s1)))
    





